from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.decorators import role_required
from app.models import Complaint
from app.forms import AdminReviewForm
from app.extenshions import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/complaint/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def review_complaint(id):
    complaint = Complaint.query.get_or_404(id)
    form = AdminReviewForm()

    if form.validate_on_submit():
        complaint.admin_review = form.admin_review.data

        if form.submit_approve.data:
            complaint.status = 'Approved'

        elif form.submit_reject.data:
            complaint.status = 'Rejected'

        db.session.commit()
        return redirect(url_for('admin.all_complaints'))

    return render_template(
        'review_complaint.html',
        complaint=complaint,
        form=form
    )
