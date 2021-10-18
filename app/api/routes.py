from flask import render_template, url_for, redirect, current_app, request, jsonify
from flask import request, jsonify
from app.forms import NavigationForm, return_search_query
from app.api import bp

# Import Models
from app.view_model import Video
from app.database_logic import add_function


# AJAX Method to save to respository
@bp.route('/extension_save', methods=['POST'])
def add_resource():
    # Logic to add to database
    # 1. check if it exists
    # 2. if it exists you do user related stuff
    # (user has rated, added to repository)
    resource_id = request.form['resource_id']
    resource_understanding = request.form['resource_understanding']
    resource_like = request.form['resource_like']
    resource_link = request.form['resource_link']
    resource_tags = request.form['resource_tags']
    current_app.logger.info(f"""Saving resource with
                                ID: {resource_id}
                                Understanding: {resource_understanding}
                                Like: {resource_like}
                                Link: {resource_link}
                                Tags: {resource_tags}
                             """)

    new_resource = Video(link=resource_link)

    # TODO: Get active language, level from user
    try:
        language = 'French'
        level = 'Intermediate 1'

        add_function("Leon Wu", language, resource_like,
                     resource_understanding, level, resource_tags, new_resource)
        r = {'success': 200}
    except Exception as inst:
        print(inst)
        r = {'fail': 500}
    return jsonify(r)


# AJAX Method to save to respository
@bp.route('/save_resource', methods=['POST'])
def save_resource():
    resource_id = request.form['resource_id']
    # Logic to add to database
    current_app.logger.info(f"Saving resource with ID: {resource_id}")
    success = True
    # Return a small success/fail message
    if success:
        r = {'success': 200}
    else:
        r = {'fail': 500}
    return jsonify(r)


@bp.route('/rate_resource', methods=['POST'])
def rate_resource():
    resource_id = request.form['resource_id']
    resource_rate = request.form['rating']
    if request.form['rate_type'] == "like":
        resource_rate_type = "like"
    else:
        resource_rate_type = "understanding"
    current_app.logger.info(f"""Saving resource with
                                ID: {resource_id}
                                Rate: {resource_rate}
                                Type: {resource_rate_type}
                             """)
    success = True
    if success:
        r = {'success': 200}
    else:
        r = {'fail': 500}
    return jsonify(r)
