from fastapi import FastAPI, HTTPException
from typing import List
from model import Doctor, Patient

app = FastAPI()

# In-memory storage
doctors_db = []
patients_db = []

# DOCTOR APIs 

@app.post("/doctors", response_model=Doctor)
def create_doctor(doctor: Doctor):
    doctors_db.append(doctor)
    return doctor

@app.get("/doctors", response_model=List[Doctor])
def get_doctors():
    return doctors_db

@app.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    if doctor_id < 0 or doctor_id >= len(doctors_db):
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctors_db[doctor_id]

# PATIENT APIs 

@app.post("/patients", response_model=Patient)
def create_patient(patient: Patient):
    patients_db.append(patient)
    return patient

@app.get("/patients", response_model=List[Patient])
def get_patients():
    return patients_db 
