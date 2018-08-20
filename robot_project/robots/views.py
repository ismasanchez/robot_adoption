from flask import Blueprint, render_template, url_for, redirect, request, jsonify
from robot_project import db
from robot_project.robots.models import Robot
from robot_project.robots.forms import AddForm

robots_blueprint = Blueprint("robots", __name__, template_folder="templates")


@robots_blueprint.route('/add_robot', methods=['GET', 'POST'])
def add_robot():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Puppy to database
        new_robot = Robot(name)
        db.session.add(new_robot)
        db.session.commit()

        return redirect(url_for('robots.list'))

    return render_template('add_robot.html', form=form)


@robots_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    robots = Robot.query.all()
    return render_template('list.html', robots=robots)


@robots_blueprint.route('/delete', methods=['POST'])
def del_robot():
    robot_id = request.form['robot_id']
    robot = Robot.query.get(robot_id)
    db.session.delete(robot)
    db.session.commit()
    return jsonify({'robot_id': robot_id})
