from django import forms


class User(forms.Form):
    userID = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    middle_name = forms.CharField(max_length=250)
    job_title = forms.CharField(max_length=250)
    email = forms.EmailField(label='Email')
    office_phone = forms.CharField(max_length=250)
    phone_prefix = forms.CharField(max_length=250)
    clientID = forms.CharField(max_length=250)


class Client(forms.Form):
    client_ID = forms.CharField(max_length=250)
    client_name = forms.CharField(max_length=250)
    client_type = forms.CharField(max_length=250)


class Location(forms.Form):
    location_ID = forms.CharField(max_length=250)
    address1 = forms.CharField(max_length=250)
    address2 = forms.CharField(max_length=250)
    city = forms.CharField(max_length=250)
    state = forms.CharField(max_length=250)
    postal_code = forms.CharField(max_length=250)
    country = forms.CharField(max_length=250)
    phone_number = forms.CharField(max_length=250)
    fax_number = forms.CharField(max_length=250)
    client_ID = forms.CharField(max_length=250)


class Product(forms.Form):
    model_number = forms.CharField(max_length=250)
    product_name = forms.CharField(max_length=250)
    cell_technology = forms.CharField(max_length=250)
    cell_manufacturer = forms.CharField(max_length=250)
    number_of_cells = forms.CharField(max_length=250)
    number_of_cells_in_series = forms.CharField(max_length=250)
    number_of_series_strings = forms.CharField(max_length=250)
    number_of_diodes = forms.CharField(max_length=250)
    product_length = forms.CharField(max_length=250)
    product_width = forms.CharField(max_length=250)
    product_weight = forms.CharField(max_length=250)
    superstrate_type = forms.CharField(max_length=250)
    superstrate_manufacturer = forms.CharField(max_length=250)
    substrate_type = forms.CharField(max_length=250)
    substrate_manufacturer = forms.CharField(max_length=250)
    frame_type = forms.CharField(max_length=250)
    frame_adhesive = forms.CharField(max_length=250)
    encapsulate_type = forms.CharField(max_length=250)
    encapsulate_manufacturer = forms.CharField(max_length=250)
    junction_box_type = forms.CharField(max_length=250)
    junction_box_manufacturer = forms.CharField(max_length=250)


class Certificate(forms.Form):
    certificate_number = forms.CharField(max_length=250)
    ID = forms.CharField(max_length=250)
    userID = forms.CharField(max_length=250)
    report_number = forms.CharField(max_length=250)
    issue_date = forms.CharField(max_length=250)
    standard_ID = forms.CharField(max_length=250)
    location_ID = forms.CharField(max_length=250)
    model_number = forms.CharField(max_length=250)


class Test_Standard(forms.Form):
    standard_ID = forms.CharField(max_length=250, )
    standard_name = forms.CharField(max_length=250)
    description = forms.CharField(max_length=250)
    published_date = forms.CharField(max_length=250)
