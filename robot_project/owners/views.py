from flask import Blueprint, render_template, flash, request
from robot_project import db
from robot_project.owners.models import Owner
from robot_project.robots.models import Robot
from robot_project.owners.forms import AddOwnerForm

owners_blueprint = Blueprint("owners", __name__, template_folder="templates")


@owners_blueprint.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    form = AddOwnerForm()
    robot_id = request.args.get('robot_id')
    if not robot_id:
        form.robot_id.choices = [(r.id, f'Robot ID {r.id} with name {r.name}')
                                 for r in Robot.query.order_by('id') if not r.owner]
        print(form.robot_id.choices)
    else:
        r = Robot.query.get(robot_id)
        form.robot_id.choices = [(r.id, f'Robot ID {r.id} with name {r.name}')]
        print(form.robot_id.choices)

    if form.validate_on_submit():
        name = form.name.data
        robot_id = form.robot_id.data
        robot_selected = Robot.query.get(robot_id)
        if robot_selected:
            new_owner = Owner(name, robot_id)
            db.session.add(new_owner)
            db.session.commit()
            flash(f"Dear {new_owner.name} you just adopted a new robot!")
        else:
            flash(
                f"It seems the robot with id {robot_id} is not in our database, try again!")
    return render_template('add_owner.html', form=form, robot_id=robot_id)
