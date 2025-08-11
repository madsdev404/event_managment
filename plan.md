# Plan for Event Management System: Phase 2 Features & Refinements

This plan outlines the steps to complete the `event_management` project, bringing it in line with the features and structure of the `demo` project.

## 1. Project Structure and Core App

- **Create a `core` app:** This app will house the main templates and views for static pages.
- **Move `home` view:** Relocate the `HomeView` from the `events` app to the new `core` app.
- **Create static page views and templates:** Implement views and templates for the following pages, mirroring the `demo` project's structure:
    - `features.html`
    - `pricing.html`
    - `about.html`
    - `contact.html` (including the email sending logic)
    - `no_permission.html`
- **Update URL structure:**
    - Create a `urls.py` in the `core` app.
    - Include the `core.urls` in the main `event_management/urls.py`.
    - Move the home URL pattern to `core/urls.py`.

## 2. Settings and Configuration

- **Update `settings.py`:**
    - **Database:** Switch from SQLite to PostgreSQL.
    - **Email:** Configure the email backend with the necessary settings (host, port, user, password).
    - **Static and Media Files:** Ensure `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL`, and `MEDIA_ROOT` are correctly configured.
    - **Installed Apps:** Add `'widget_tweaks'` to the `INSTALLED_APPS` list.
    - **Login/Logout URLs:** Define `LOGIN_URL`, `LOGIN_REDIRECT_URL`, and `LOGOUT_REDIRECT_URL`.

## 3. Templates and Styling

- **Create a `base.html`:** Develop a base template in the `templates` directory of the `core` app. This template should include:
    - A consistent navigation bar.
    - A footer.
    - Blocks for content, title, and scripts.
- **Update existing templates:** All existing templates should extend the new `base.html`.
- **Style forms:** Use `widget_tweaks` to improve the styling of all forms in the project.
- **Improve UI/UX:** Enhance the overall user interface and experience by applying consistent styling and layout across all pages.

## 4. Refine Existing Apps

- **`users` app:**
    - **Templates:** Move the `users` app's templates into a `templates/users` directory.
    - **Styling:** Apply the new `base.html` and `widget_tweaks` to the `signup.html` and `login.html` templates.
- **`events` app:**
    - **Templates:** Move the `events` app's templates into a `templates/events` directory.
    - **Styling:** Apply the new `base.html` and `widget_tweaks` to all templates in the `events` app.
    - **URLs:** Clean up the URL structure to be more organized.

## 5. Final Touches

- **`README.md`:** Update the `README.md` file with detailed instructions on how to set up and run the project.
- **`.env` file:** Create a `.env.example` file to show the required environment variables.
- **`requirements.txt`:** Ensure the `requirements.txt` file is up-to-date with all necessary dependencies.