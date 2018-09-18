from .forms import ProfileForm
from ..models import User,Profile
from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from flask_login import login_required,current_user
from .. import photos, db
from datetime import datetime


@main.route('/profile/add',methods = ['GET','POST'])
@login_required
def new_profile():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = ProfileForm()

    if form.validate_on_submit():
        teamname = form.teamname.data
        vision = form.vision.data
        mission = form.mission.data
        members = form.members.data

        new_profile = Profile(teamname=teamname,vision=vision,mision=mission,members=members,user_id=current_user.id)
        new_profile.save_profile()
        flash('Profile has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('new_profile.html', profile_form = form)