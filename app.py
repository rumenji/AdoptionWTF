from flask import Flask, render_template, flash, redirect
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template ('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        print(data)
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {pet.name} as available pet!")

        return redirect('/')
    
    else:
        return render_template('add_pet.html', form = form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()

        flash(f"Edited {pet.name}!")

        return redirect('/')
    
    else:
        return render_template('edit_pet.html', form = form, pet=pet)

