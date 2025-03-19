# Tours and Travels Management System

        This is a Python-based Tours and Travels Management System that allows users to book trips, view packages, and manage their accounts. Admins can manage packages, flights, hotels, users, bookings, and payments. The system uses MySQL for database management and provides a command-line interface for interaction.

        ## Features

        ### User Features
        - **Sign Up**: Register as a new user.
        - **Log In**: Log in with existing credentials.
        - **Book a Trip**: Start the booking process for a custom trip.
        - **View Packages**: View available travel packages and book them.
        - **Account Info**: View personal account information and booking history.
        - **Log Out**: Log out from the user interface.

        ### Admin Features
        - **Sign Up**: Register as a new admin.
        - **Log In**: Log in with admin credentials.
        - **View Data**: View data related to packages, flights, hotels, users, bookings, and payments.
        - **Visualize Data**: Generate line and bar graphs for data visualization.
        - **Manage Packages**: Add, delete, and update travel packages.
        - **Manage Flights**: Add, delete, and update flight details.
        - **Manage Hotels**: Add, delete, and update hotel details.
        - **Log Out**: Log out from the admin interface.

        ## Installation

        1. **Clone the repository**:
            ```sh
            git clone https://github.com/geekgod382/Tours-and-Travels-Project.git
            ```

        2. **Navigate to the project directory**:
            ```sh
            cd Tours_n_Travels
            ```

        3. **Install the required dependencies**:
            ```sh
            pip install -r requirements.txt
            ```

        4. **Set up the MySQL database**:
            - Create a database named `Tours_and_Travels`.
            - Create the required tables with appropriate attributes

        5. **Run the application**:
            ```sh
            python Tours_n_Travels.py
            ```

        ## Dependencies

        - Python 3.x
        - MySQL Connector
        - Pandas
        - Tabulate
        - Matplotlib

        ## Database Schema

        The database schema includes the following tables:
        - `admin`: Stores admin credentials.
        - `users`: Stores user information.
        - `packages`: Stores travel package details.
        - `flights`: Stores flight details.
        - `hotels`: Stores hotel details.
        - `custom_booking`: Stores custom trip bookings.
        - `package_bookings`: Stores package bookings.
        - `payments`: Stores payment details.

        ## Usage

        1. **Admin Mode**:
            - Choose `Admin` mode from the main menu.
            - Sign up or log in with admin credentials.
            - Manage packages, flights, hotels, users, bookings, and payments.
            - Visualize data using graphs.

        2. **User Mode**:
            - Choose `User` mode from the main menu.
            - Sign up or log in with user credentials.
            - Book trips, view packages, and manage account information.

        3. **Exit**:
            - Choose `Exit` from the main menu to close the application.

        ## Acknowledgements

        - [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
        - [Pandas](https://pandas.pydata.org/)
        - [Tabulate](https://pypi.org/project/tabulate/)
        - [Matplotlib](https://matplotlib.org/)
