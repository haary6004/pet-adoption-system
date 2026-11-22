# Paw Haven: quick presentation notes

## A short demo

1. Open the home page and show the sample pets.
2. Create a customer account, then send an adoption request.
3. Sign in as a staff user and open the staff dashboard.
4. Open Django admin to show pet records and change a request's status.

Use your own accounts during the demo. Do not show passwords.

## Explain it simply

“Paw Haven is a Django pet adoption site. The home page reads available pets from the database. A customer signs up and submits an adoption request. Django saves the request with links to the customer and the pet. Staff can review requests and manage pet records in the admin site.”

## What to understand

- A **model** describes the information Django stores. `Pet` stores pet details; `AdoptionRequest` stores who asked about which pet.
- A **view** handles a page request. It gets data and chooses which page to show.
- A **template** is the HTML page that the browser displays.
- A **URL** connects an address, such as `/`, to a view.
- A **migration** is Django's saved instruction for creating or changing database tables.
- A **foreign key** is a database link. Each adoption request points to one pet and one customer.

## Just recognize

- `INSTALLED_APPS` tells Django which project apps to load.
- `urls.py` files connect web addresses to views.
- `@login_required` means a person must sign in before using that view.
- `is_staff` is used to restrict the dashboard to staff accounts.
- `csrf_token` helps protect forms that send information.

## No need to memorize

- The exact CSS values, every setting, or each line of Django's built-in login form.
- It is okay to open the code and explain the part you are showing.

## Be accurate about the current state

The local project has a working database and sample pets. A public GitHub repository and hosted deployment link still need to be created from the student's own connected accounts. If those are not ready by submission, say so plainly and show the local app.
