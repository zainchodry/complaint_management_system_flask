from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Complaint
from app.forms import ComplaintForm, CommentForm
from app.extenshions import db

complaint_bp = Blueprint('complaints', __name__)

@complaint_bp.route('/')
@login_required
def dashboard():
    complaints = Complaint.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', complaints=complaints)

@complaint_bp.route('/create', methods=['GET','POST'])
@login_required
def create():
    form = ComplaintForm()
    if form.validate_on_submit():
        c = Complaint(
            title=form.title.data,
            description=form.description.data,
            user_id=current_user.id
        )
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('complaints.dashboard'))
    return render_template('create.html', form=form)
