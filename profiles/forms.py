from django import forms
from django.contrib.auth.models import User
from .models import Profile, ProfileImage, SupportingDocuments
from authenticate.data_validator import *

class UpdateProfileInformationForm(forms.Form):
	email = forms.CharField(max_length=150)
	first_name = forms.CharField(max_length=150)
	last_name = forms.CharField(max_length=150)
	idnumber  = forms.CharField(max_length=13)
	phone = forms.CharField(max_length=10)
	maritial_status = forms.CharField(max_length=10)
	race = forms.CharField(max_length=15)
	r_phone = forms.CharField(max_length=10)
	
	def validate_names(self,name):
		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 3:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		if ' ' in first_name :
			raise forms.ValidationError("Spaces not allowed in First Name")
		return self.validate_names(first_name)

	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		if ' ' in last_name :
			raise forms.ValidationError("Spaces not allowed in Last Name")
		return self.validate_names(last_name)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if ' ' in email :
			raise forms.ValidationError("Spaces not allowed in email")
		if not validate_email(email):
			raise forms.ValidationError(f"Email: {email} in Invalid")
		new_email = email.split('@')
		if len(new_email[0]) < 3:
			raise forms.ValidationError("Email length is Invalid") 
		
		return email

	def clean_maritial_status(self):
		maritial_status = self.cleaned_data.get('maritial_status')
		if ' ' in maritial_status :
			raise forms.ValidationError("Spaces not allowed in maritial status")
		return self.validate_names(maritial_status)

	def clean_race(self):
		race = self.cleaned_data.get('race')
		if race == "empty":
			return race
		if ' ' in race :
			raise forms.ValidationError("Spaces not allowed in race")
		return self.validate_names(race)

	def clean_disability(self):
		linkedin_profile = self.cleaned_data.get('linkedin_profile')
		
		if linkedin_profile == "none" or linkedin_profile =="" or linkedin_profile == None or linkedin_profile ==" ":
			return linkedin_profile
		pattern = re.compile(r'^(https?:\/\/)?(www\.)?linkedin\.com\/(in|pub|company)\/[A-Za-z0-9_-]+\/?$')
		if not bool(pattern.match(linkedin_profile)) :
		 	raise forms.ValidationError("linkedin url is invalid")

		personal_website = self.cleaned_data.get('personal_website')
		if personal_website == "none" or personal_website =="" or personal_website == None or personal_website ==" ":
			return personal_website
		pattern = re.compile(r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/[a-zA-Z0-9-]*)*\/?$')
		if not bool(pattern.match(personal_website)):
			raise forms.ValidationError('your personal website url is invalid')

		return self.validate_names(disability)

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		r_phone = self.cleaned_data.get('r_phone')
		if phone == "empty":
			return phone
		if ' ' in phone :
			raise forms.ValidationError("Spaces not allowed in email")
		exist = User.objects.filter(profile__phone=phone).exists()
		if exist:
			user = User.objects.get(profile__phone=phone)
			print(user.profile.phone, r_phone)
			if user.profile.phone == r_phone:
				pass
			else:
				raise forms.ValidationError("phone Number Already taken")
		if not validate_south_african_phone_number(phone):
			raise forms.ValidationError("Phone number is not a valid south african number or its empty")
		return phone

	# def clean_username(self):
	# 	username = self.cleaned_data.get('username')
	# 	if ' ' in username :
	# 		raise forms.ValidationError("Spaces not allowed in Username")
	# 	return self.validate_names(username)

	# def clean_password(self):
		
	# 	password = self.cleaned_data.get('password')
	# 	password2 = self.cleaned_data.get('password2')
	# 	first_name = self.cleaned_data.get('first_name') 
	# 	# username = self.cleaned_data.get('username')
		
		
	# 	pattern = r"[~`+=\-/\*\\|}{\[\];'\?.,]"
	# 	matches = re.findall(pattern, password)

	# 	if matches:
			
	# 		raise forms.ValidationError("Password Format is not allowed")
		
	# 	if len(password) < 6:
	# 		raise forms.ValidationError("Password is too short")

	# 	char = [char for char in password if char.isdigit()]
	# 	if len(char) < 1:
	# 		raise forms.ValidationError("Password must contain at least one Number")
		
	# 	if first_name in password: #or username in password:
	# 		raise forms.ValidationError("Password cannot contain username of first name")  
	# 	return password


	def clean_idnumber(self):
		idnumber = self.cleaned_data.get('idnumber')
		# r_idnum = self.cleaned_data.get('r_idnum')
		# validate = ValidateIdNumber(idnumber)
		# is_valid = validate.validateSAID()
		# exist = User.objects.filter(profile__idnumber=idnumber).exists()
		# if exist:
		# 	user = User.objects.get(profile__idnumber=idnumber)
			
		# 	if user.profile.idnumber != r_idnum:
		# 		pass
		# 	else:
		#  		raise forms.ValidationError("Id Number Already taken")
			
		# if not is_valid:
		# 	raise forms.ValidationError("Provide ID Number is not a valid South African ID Number")
		return idnumber

class UpdateQualificationForm(forms.Form):
	highest_qualification = forms.CharField(max_length=225)
	field_of_study = forms.CharField(max_length=225)
	institution = forms.CharField(max_length=225) 
	year_obtained =  forms.CharField(max_length=225)
	status =  forms.CharField(max_length=225)
	grade = forms.CharField(max_length=100)

	def validate_names(self,name):
		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 2:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name

	def clean_highest_qualification(self):
		highest_qualification = self.cleaned_data.get('highest_qualification')
		return self.validate_names(highest_qualification)

	def clean_field_of_study(self):
		field_of_study = self.cleaned_data.get('field_of_study')
		return self.validate_names(field_of_study)
 	
	def clean_institution(self):
 		institution = self.cleaned_data.get('institution')
 		if institution == "":
 			raise forms.ValidationError('institution cannot be empty ')
 		return self.validate_names(institution)

	def clean_grade(self):
 		grade = self.cleaned_data.get('grade')
 		if grade == "":
 			raise forms.ValidationError("grade cannot be empty")
 		return self.validate_names(grade)

	def clean_year_obtained(self):
 		year_obtained = self.cleaned_data.get('year_obtained')
 		if year_obtained == "":
 			raise forms.ValidationError("year obtained cannot be empty")
 		return self.validate_names(year_obtained)
 	
	def clean_status(self):
		status = self.cleaned_data.get('status')
		if status == "":
			raise forms.ValidationError("academic status cannot be empty")
		return self.validate_names(status)
	
# class UpdateLanguageForm(forms.Form):
# 	language = forms.CharField(max_length=225)
# 	reading_proficiency = forms.CharField(max_length=225)
# 	writing_proficiency = forms.CharField(max_length=225)
# 	speaking_proficiency = forms.CharField(max_length=225)

# 	def validate_names(self,name):
# 		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
# 		matches = re.findall(pattern, name)
# 		if matches:
# 			raise forms.ValidationError("No special characters allowed")
# 		if len(name) < 2:
# 			raise forms.ValidationError(f"Name:{name} is too short")
# 		try:
# 			str(name)
# 		except Exception as e:
# 			raise forms.ValidationError(e)
# 		return name

# 	def clean_language(self):
# 		language = self.cleaned_data.get('language')
# 		return self.validate_names(language)

# 	def clean_writing_proficiency(self):
# 		writing_proficiency = self.cleaned_data.get('writing_proficiency')
# 		return self.validate_names(writing_proficiency)
# 	def clean_reading_proficiency(self):
# 		reading_proficiency = self.cleaned_data.get('reading_proficiency')
# 		return self.validate_names(reading_proficiency)
# 	def clean_speaking_proficiency(self):
# 		speaking_proficiency = self.cleaned_data.get('speaking_proficiency')
# 		return self.validate_names(speaking_proficiency)


# class UpdateSkillsForm(forms.Form):
# 	skill = forms.CharField(max_length=225)
# 	level = forms.CharField(max_length=225)
	
# 	def validate_names(self,name):
# 		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
# 		matches = re.findall(pattern, name)
# 		if matches:
# 			raise forms.ValidationError("No special characters allowed")
# 		if len(name) < 2:
# 			raise forms.ValidationError(f"Name:{name} is too short")
# 		try:
# 			str(name)
# 		except Exception as e:
# 			raise forms.ValidationError(e)
# 		return name

# 	def clean_skill(self):
# 		skill = self.cleaned_data.get('skill')
# 		return self.validate_names(skill)
		
# 	def clean_level(self):
# 		level = self.cleaned_data.get('level')
# 		return self.validate_names(level)

class UpdateAddressInformationForm(forms.Form):
	street_address_line = forms.CharField(max_length=225)
	city = forms.CharField(max_length=225)
	province = forms.CharField(max_length=225)
	postal_code = forms.CharField(max_length=6)

	def validate_names(self,name):
		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 3:
			raise forms.ValidationError(f" Address :{name} is too short")
		return name

	def clean_street_address_line(self):
		street_address_line = self.cleaned_data.get('street_address_line')
		return self.validate_names(street_address_line)

	def clean_street_address_line1(self):
		street_address_line = self.cleaned_data.get('street_address_line')
		return self.validate_names(street_address_line)

	def clean_city(self):
		city = self.cleaned_data.get('city')
		return self.validate_names(city)

	def clean_province(self):
		province = self.cleaned_data.get('province')
		return self.validate_names(province)

	def clean_postal_code(self):
		postal_code = self.cleaned_data.get('postal_code')
		if len(postal_code) < 3 :
			raise forms.ValidationError("Postal code is too short")
		try:
			int(postal_code)
		except:
			raise forms.ValidationError("Postal code must integers")

class UpdateWorkingExpereinceForm(forms.Form):
	job_title = forms.CharField(max_length=225)
	company = forms.CharField(max_length=225)
	location = forms.CharField(max_length=225)
	description = forms.CharField(max_length=6)

	def validate_names(self,name):
		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 3:
			raise forms.ValidationError(f" Address :{name} is too short")
		return name

	def clean_job_title(self):
		job_title = self.cleaned_data.get('job_title')
		return self.validate_names(job_title)

	def clean_street_address_line1(self):
		street_address_line = self.cleaned_data.get('street_address_line')
		return self.validate_names(street_address_line)

	def clean_company(self):
		company = self.cleaned_data.get('company')
		return self.validate_names(company)

	def clean_location(self):
		location = self.cleaned_data.get('location')
		return self.validate_names(location)

	def clean_description(self):
		description = self.cleaned_data.get('description')
		if len(description) < 3 :
			raise forms.ValidationError(" job description too short")
		return self.validate_names(clean_description)

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = ProfileImage
		fields = ['image']

class DocumentUploadForm(forms.ModelForm):
	class Meta:
		model = SupportingDocuments
		fields = ['document','document_type']



class AddStaffForm(forms.Form):
	
	username = forms.CharField(max_length=225)
	email = forms.CharField(max_length=225)
	job_title = forms.CharField(max_length=225)
	department = forms.CharField(max_length=225)
	phone = forms.CharField(max_length=225)
	idnumber = forms.CharField(max_length=225)
	password = forms.CharField(max_length=225)

	rate = forms.CharField(max_length=225)
	start_time = forms.CharField(max_length=225)
	end_time = forms.CharField(max_length=225)

	def validate_names(self,name):
     
		pattern = r"[~`+!@#$%^&*()=\/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 2:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name
	
	def clean_idnumber(self):
		idnumber = self.cleaned_data.get('idnumber')
		validate = ValidateIdNumber(idnumber)
		is_valid = validate.validateSAID()
		exist = User.objects.filter(profile__idnumber=idnumber).exists()
		# if exist:
		# 	raise forms.ValidationError("Id Number Already taken")
		
		if ' ' in idnumber :
			raise forms.ValidationError("Spaces not allowed ")

		# if not is_valid:
		# 	raise forms.ValidationError("Provide ID Number is not a valid South African ID Number")
		return idnumber

	def clean_department(self):
 		department = self.cleaned_data.get('department')
 		if department == "":
 			raise forms.ValidationError('Job Title cannot be empty ')
 		if department not in ["HR","IT","MANAGER","FINANCE", "ADMINISTRATOR"] :
 			raise forms.ValidationError('department is invalid ')

 		return self.validate_names(department)



	def clean_job_title(self):
 		job_title = self.cleaned_data.get('job_title')
 		if job_title == "":
 			raise forms.ValidationError('Job Title cannot be empty ')
 		return self.validate_names(job_title)
 	
	def first_name(self):
 		first_name = self.cleaned_data.get('first_name')
 		if first_name == "" or first_name == None:
 			return first_name
 		return self.validate_names(first_name)
 	
	def last_name(self):
 		last_name = self.cleaned_data.get('last_name')
 		if last_name == "" or last_name == None:
 			return last_name
 		return self.validate_names(last_name)

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		r_phone = self.cleaned_data.get('r_phone')
		if ' ' in phone :
			raise forms.ValidationError("Spaces not allowed in phone number")
		exist = User.objects.filter(profile__phone=phone).exists()
		if exist:
			user = User.objects.get(profile__phone=phone)
			print(user.profile.phone, r_phone)
			if user.profile.phone == r_phone:
				pass
			else:
				raise forms.ValidationError("phone Number Already taken")
		
		if not validate_south_african_phone_number(phone):
			raise forms.ValidationError("Phone number is not a valid south african number or its empty")
		return phone


	def clean_username(self):
		username = self.cleaned_data.get('username')
		self.first_name()
		self.last_name()
		if ' ' in username :
			raise forms.ValidationError("Spaces not allowed ")
		exist = User.objects.filter(username=username).exists()
		if exist:
			raise forms.ValidationError(f" {username} is already taken")
		return self.validate_names(username)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if ' ' in email :
			raise forms.ValidationError("Spaces not allowed ")
		if not validate_email(email):
			raise forms.ValidationError(f": {email} in Invalid")
		new_email = email.split('@')
		if len(new_email[0]) < 3:
			raise forms.ValidationError(" length is Invalid") 
		exist = User.objects.filter(email=email).exists()
		if exist:
			raise forms.ValidationError(f"Email: {email} is already taken")
		return email

	def clean_password(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2') 
		username = self.cleaned_data.get('username')
		pattern = r"[~`+=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, password)

		if matches:		
			raise forms.ValidationError(" Format is not allowed")

		if ' ' in password :
			raise forms.ValidationError("Spaces not allowed ")

		if len(password) < 6:
			raise forms.ValidationError(" is too short")

		char = [char for char in password if char.isdigit()]
		if len(char) < 1:
			raise forms.ValidationError(" must contain at least one Number")
		try:
			if username in password: #or username in password:
				raise forms.ValidationError(" cannot contain username ")  
		except:
			pass
		return password


class UpdateStaffForm(forms.Form):
	
	username = forms.CharField(max_length=225)
	email = forms.CharField(max_length=225)
	job_title = forms.CharField(max_length=225)
	department = forms.CharField(max_length=225)
	phone = forms.CharField(max_length=225)
	idnumber = forms.CharField(max_length=225)

	rate = forms.CharField(max_length=225)
	start_time = forms.CharField(max_length=225)
	end_time = forms.CharField(max_length=225)

	def validate_names(self,name): 
		pattern = r"[~`+!@#$%^&*()=\/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 2:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name
	
	def clean_idnumber(self):
		idnumber = self.cleaned_data.get('idnumber')
		validate = ValidateIdNumber(idnumber)
		is_valid = validate.validateSAID()
		exist = User.objects.filter(profile__idnumber=idnumber).exists()	
		if ' ' in idnumber :
			raise forms.ValidationError("Spaces not allowed ")
		# if not is_valid:
		# 	raise forms.ValidationError("Provide ID Number is not a valid South African ID Number")
		return idnumber

	def clean_department(self):
 		department = self.cleaned_data.get('department')
 		if department == "":
 			raise forms.ValidationError('Job Title cannot be empty ')
 		if department not in ["HR","IT","MANAGER","FINANCE", "ADMINISTRATOR"] :
 			raise forms.ValidationError('department is invalid ')
 		return self.validate_names(department)

	def clean_job_title(self):
 		job_title = self.cleaned_data.get('job_title')
 		if job_title == "":
 			raise forms.ValidationError('Job Title cannot be empty ')
 		return self.validate_names(job_title)
 	
	def first_name(self):
 		first_name = self.cleaned_data.get('first_name')
 		if first_name == "" or first_name == None:
 			return first_name
 		return self.validate_names(first_name)
 	
	def last_name(self):
 		last_name = self.cleaned_data.get('last_name')
 		if last_name == "" or last_name == None:
 			return last_name
 		return self.validate_names(last_name)

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		r_phone = self.cleaned_data.get('r_phone')
		if ' ' in phone :
			raise forms.ValidationError("Spaces not allowed in phone number")
		exist = User.objects.filter(profile__phone=phone).exists()
		if not validate_south_african_phone_number(phone):
			raise forms.ValidationError("Phone number is not a valid south african number or its empty")
		return phone


	def clean_username(self):
		username = self.cleaned_data.get('username')
		self.first_name()
		self.last_name()
		if ' ' in username :
			raise forms.ValidationError("Spaces not allowed ")	
		return self.validate_names(username)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if ' ' in email :
			raise forms.ValidationError("Spaces not allowed ")
		if not validate_email(email):
			raise forms.ValidationError(f": {email} in Invalid")
		new_email = email.split('@')
		if len(new_email[0]) < 3:
			raise forms.ValidationError(" length is Invalid") 
		return email

	def clean_password(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2') 
		username = self.cleaned_data.get('username')
		pattern = r"[~`+=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, password)

		if matches:		
			raise forms.ValidationError(" Format is not allowed")

		if ' ' in password :
			raise forms.ValidationError("Spaces not allowed ")

		if len(password) < 6:
			raise forms.ValidationError(" is too short")

		char = [char for char in password if char.isdigit()]
		if len(char) < 1:
			raise forms.ValidationError(" must contain at least one Number")
		try:
			if username in password: #or username in password:
				raise forms.ValidationError(" cannot contain username ")  
		except:
			pass
		return password

	def validate_rate(self,rate): 
		pattern = r"[~`+!@#$%^&*()=\/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, rate)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		try:
			float(rate)
		except Exception as e:
			raise forms.ValidationError(e)
		return rate
	
	def validate_time(self, time_str):
    		# Regular expression for hh:mm format
		pattern = r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
		if re.match(pattern, time_str):
			return time_str
		else:
			raise forms.ValidationError("Error: Time must be in hh:mm format within the 24-hour range (00:00 to 23:59).")
		return time_str

	def clean_rate(self):
		rate = self.cleaned_data.get('rate')
		if ' ' in rate :
			raise forms.ValidationError("Spaces not allowed ")
		return self.validate_rate(rate)

	def clean_start_time(self):
		start_time = self.cleaned_data.get('start_time')
		if ' ' in start_time :
			raise forms.ValidationError("Spaces not allowed ")
		return self.validate_time(start_time)

	def clean_end_time(self):
		end_time = self.cleaned_data.get('end_time')
		if ' ' in end_time :
			raise forms.ValidationError("Spaces not allowed ")
		return self.validate_time(end_time)


	
	

class AtendanceForm(forms.Form):
	status = forms.CharField(max_length=225)
	
	def validate_names(self,name): 
		pattern = r"[~`+!@#$%^&*()=\/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 2:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name

	def clean_status(self):
		status = self.cleaned_data.get('status')
		if " " in status:
			raise forms.ValidationError("Spaces not allowed ")
		if status not in ['pending', 'rejected', 'approved']:
			raise forms.ValidationError("Invalid status name")
		return self.validate_names(status)   


class LeaveForm(forms.Form):
	# status = forms.CharField(max_length=225)
	leave_type = forms.CharField(max_length=225)
	message = forms.CharField(max_length=225)

	
	def validate_names(self,name): 
		pattern = r"[~`+!@#$%^&*()=\/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 2:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name

	def clean_leave_type(self):
		leave_type = self.cleaned_data.get('leave_type')
		if leave_type not in ['Martenity Leave', 'Holiday Leave', 'Sick Leave', 'Religious Leave', 'Family and Medical Leave']:
			raise forms.ValidationError("Invalid leave type ") 
		return self.validate_names(leave_type)
	# def clean_status(self):
	# 	status = self.cleaned_data.get('status')
	# 	if status not in ['Pending', 'Rejected', 'Approved']:
	# 		raise forms.ValidationError("Invalid leave type ") 
	# 	return self.validate_names(status)
	
	def clean_message(self):
		message = self.cleaned_data.get('message')
		return self.validate_names(message)



