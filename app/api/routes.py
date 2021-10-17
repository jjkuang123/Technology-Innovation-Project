from flask import render_template, url_for, redirect, current_app, request, jsonify
from flask import request, jsonify
from app.forms import NavigationForm, return_search_query
from app.api import bp

# Import Models
from app.view_model import Video


# AJAX Method to save to respository
@bp.route('/extension_save', methods=['POST'])
def add_resource():
    # Logic to add to database
    # 1. check if it exists
    # 2. if it exists you do user related stuff
    # (user has rated, added to repository)
    resource_id = request.form['resource_id']
    resource_like = request.form['like']
    resource_usefulness = request.form['usefulness']
    resource_link = request.form['link']
    current_app.logger.info(f"""Saving resource with
                                ID: {resource_id}
                                Like: {resource_like}
                                Use: {resource_usefulness}
                                Link: {resource_link}
                             """)
    success = True
    # Return a small success/fail message
    if success:
        r = {'success': 200}
    else:
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
        resource_rate_type = "usefulness"
    current_app.logger.info(f"""Saving resource with
                                ID: {resource_id}
                                Like: {resource_rate}
                                Type: {resource_rate_type}
                             """)
    success = True
    if success:
        r = {'success': 200}
    else:
        r = {'fail': 500}
    return jsonify(r)
