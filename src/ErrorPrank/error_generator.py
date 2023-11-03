def generate_stacktrace(numlines = 8, is_silly=False):
    import random
    #information about various aspects of the stack trace that will be randomly chosen from these lists
    func_names = ["calculate_total_price", "validate_user_input", "generate_report", "process_data", "fetch_data_from_api", "parse_config_file", "send_email_notification", "authenticate_user", "update_database_record", "search_products", "create_user_profile", "generate_random_password", "validate_email_address", "format_date_string", "calculate_average_score", "generate_unique_id", "encrypt_password", "decrypt_data", "parse_csv_file", "validate_credit_card", "sort_list_of_objects", "check_file_existence", "read_json_data", "write_to_database", "search_customer_orders", "calculate_discounted_price", "generate_invoice_number", "parse_xml_data", "validate_phone_number", "create_order_history", "generate_api_key", "validate_input_length", "send_sms_notification", "check_user_permissions", "parse_html_content", "generate_unique_filename", "calculate_tax_amount", "validate_user_age", "parse_response_data", "calculate_shipping_cost", "format_currency", "validate_url_format", "send_push_notification", "check_file_permissions", "parse_yaml_config", "calculate_interest_rate", "validate_ip_address", "parse_excel_data", "validate_user_address", "generate_access_token", "calculate_profit_margin", "parse_image_metadata", "validate_product_code", "generate_auth_token", "calculate_percentage", "parse_binary_data", "validate_social_security_number", "generate_unique_barcode", "calculate_gross_salary", "parse_database_response", "validate_file_extension", "generate_signature", "calculate_moving_average", "validate_discount_code", "parse_sensor_data", "calculate_cubic_volume", "generate_short_url", "validate_color_code", "parse_weather_data", "calculate_area_of_circle", "validate_vehicle_registration", "generate_product_sku", "parse_audio_metadata", "calculate_quadratic_equation", "validate_dns_address", "generate_user_id", "parse_network_data", "calculate_bmi", "validate_mac_address", "generate_transaction_id", "calculate_fibonacci_sequence", "validate_oauth_token", "generate_password_hash", "parse_sensor_reading", "calculate_prime_numbers", "validate_serial_number", "generate_image_thumbnail", "parse_sensor_signals", "calculate_sha256_hash", "validate_email_domain", "generate_random_color", "parse_packet_data", "calculate_triangle_area", "validate_latitude_longitude", "generate_user_initials", "parse_error_logs", "calculate_exponential_growth", "validate_file_size", "generate_user_agent"]

    varnames = ['user_id', 'username', 'email_address', 'password', 'first_name', 'last_name', 'date_of_birth', 'address', 'city', 'state', 'zip_code', 'phone_number', 'is_active', 'is_admin', 'account_balance', 'transaction_history', 'credit_card_number', 'expiration_date', 'cvv', 'shipping_address', 'billing_address', 'product_name', 'product_id', 'price', 'quantity', 'is_in_stock', 'manufacturer', 'manufacturing_date', 'expiry_date', 'category', 'customer_orders', 'order_id', 'order_date', 'order_status', 'payment_method', 'shipping_status', 'delivery_address', 'delivery_date', 'customer_reviews', 'product_rating', 'review_date', 'reviewer_name', 'review_comment', 'is_approved', 'is_verified', 'is_published', 'creation_date', 'modification_date', 'is_deleted', 'file_name', 'file_path', 'file_size', 'file_format', 'is_private', 'access_level', 'download_count', 'upload_date', 'uploader_username', 'document_title', 'document_type', 'document_content', 'word_count', 'page_count', 'author_name', 'publication_date', 'citation_count', 'conference_name', 'conference_date', 'presentation_title', 'speaker_name', 'event_date', 'event_location', 'ticket_price', 'event_capacity', 'attendee_list', 'attendee_name', 'registration_status', 'workshop_name', 'workshop_date', 'workshop_duration', 'workshop_trainer', 'workshop_attendees', 'workshop_feedback', 'feedback_rating', 'feedback_comment', 'survey_questions', 'question_text', 'question_options', 'user_responses', 'response_text', 'response_value', 'survey_results', 'result_id', 'result_data']

    paths = ['\\Users\\pyperror\\utils\\helper_functions.py', '\\Users\\pyperror\\models\\user_model.py', '\\Users\\pyperror\\views\\home_view.py', '\\Users\\pyperror\\controllers\\data_controller.py', '\\Users\\pyperror\\tests\\test_utils.py', '\\Users\\pyperror\\api\\authentication_api.py', '\\Users\\pyperror\\scripts\\data_processing.py', '\\Users\\pyperror\\config\\config_parser.py', '\\Users\\pyperror\\utils\\string_operations.py', '\\Users\\pyperror\\models\\product_model.py', '\\Users\\pyperror\\views\\admin_view.py', '\\Users\\pyperror\\controllers\\user_controller.py', '\\Users\\pyperror\\tests\\test_models.py', '\\Users\\pyperror\\api\\data_api.py', '\\Users\\pyperror\\scripts\\report_generation.py', '\\Users\\pyperror\\config\\settings_parser.py', '\\Users\\pyperror\\utils\\file_operations.py', '\\Users\\pyperror\\models\\order_model.py', '\\Users\\pyperror\\views\\customer_view.py', '\\Users\\pyperror\\controllers\\order_controller.py', '\\Users\\pyperror\\tests\\test_views.py', '\\Users\\pyperror\\api\\payment_api.py', '\\Users\\pyperror\\scripts\\data_cleaning.py', '\\Users\\pyperror\\config\\database_config.py', '\\Users\\pyperror\\utils\\logging_utils.py', '\\Users\\pyperror\\models\\cart_model.py', '\\Users\\pyperror\\views\\cart_view.py', '\\Users\\pyperror\\controllers\\cart_controller.py', '\\Users\\pyperror\\tests\\test_controllers.py', '\\Users\\pyperror\\api\\product_api.py', '\\Users\\pyperror\\scripts\\data_analysis.py', '\\Users\\pyperror\\config\\server_config.py', '\\Users\\pyperror\\utils\\validation_utils.py', '\\Users\\pyperror\\models\\category_model.py', '\\Users\\pyperror\\views\\category_view.py', '\\Users\\pyperror\\controllers\\category_controller.py', '\\Users\\pyperror\\tests\\test_api.py', '\\Users\\pyperror\\api\\customer_api.py', '\\Users\\pyperror\\scripts\\report_analysis.py', '\\Users\\pyperror\\config\\api_config.py', '\\Users\\pyperror\\utils\\error_handling.py', '\\Users\\pyperror\\models\\supplier_model.py', '\\Users\\pyperror\\views\\supplier_view.py', '\\Users\\pyperror\\controllers\\supplier_controller.py', '\\Users\\pyperror\\tests\\test_config.py', '\\Users\\pyperror\\api\\order_api.py', '\\Users\\pyperror\\scripts\\data_visualization.py', '\\Users\\pyperror\\config\\auth_config.py', '\\Users\\pyperror\\utils\\security_utils.py', '\\Users\\pyperror\\models\\invoice_model.py', '\\Users\\pyperror\\views\\invoice_view.py', '\\Users\\pyperror\\controllers\\invoice_controller.py', '\\Users\\pyperror\\tests\\test_security.py', '\\Users\\pyperror\\api\\invoice_api.py', '\\Users\\pyperror\\scripts\\notification_system.py', '\\Users\\pyperror\\config\\email_config.py', '\\Users\\pyperror\\utils\\email_utils.py', '\\Users\\pyperror\\models\\customer_model.py', '\\Users\\pyperror\\views\\profile_view.py', '\\Users\\pyperror\\controllers\\customer_controller.py', '\\Users\\pyperror\\tests\\test_email.py', '\\Users\\pyperror\\api\\profile_api.py', '\\Users\\pyperror\\scripts\\report_export.py', '\\Users\\pyperror\\config\\report_config.py', '\\Users\\pyperror\\utils\\report_utils.py', '\\Users\\pyperror\\models\\employee_model.py', '\\Users\\pyperror\\views\\employee_view.py', '\\Users\\pyperror\\controllers\\employee_controller.py', '\\Users\\pyperror\\tests\\test_report.py', '\\Users\\pyperror\\api\\employee_api.py', '\\Users\\pyperror\\scripts\\data_import.py', '\\Users\\pyperror\\config\\import_config.py', '\\Users\\pyperror\\utils\\import_utils.py', '\\Users\\pyperror\\models\\notification_model.py', '\\Users\\pyperror\\views\\notification_view.py', '\\Users\\pyperror\\controllers\\notification_controller.py', '\\Users\\pyperror\\tests\\test_import.py', '\\Users\\pyperror\\api\\notification_api.py', '\\Users\\pyperror\\scripts\\user_management.py', '\\Users\\pyperror\\config\\user_config.py', '\\Users\\pyperror\\utils\\user_utils.py', '\\Users\\pyperror\\models\\customer_order_model.py', '\\Users\\pyperror\\views\\customer_order_view.py', '\\Users\\pyperror\\controllers\\customer_order_controller.py', '\\Users\\pyperror\\tests\\test_user_management.py', '\\Users\\pyperror\\api\\customer_order_api.py', '\\Users\\pyperror\\scripts\\data_migration.py', '\\Users\\pyperror\\config\\migration_config.py', '\\Users\\pyperror\\utils\\migration_utils.py', '\\Users\\pyperror\\models\\sales_model.py', '\\Users\\pyperror ...']

    errors = ["SyntaxError: invalid syntax", "IndentationError: unexpected indent", "NameError: name 'response_text' is not defined", "TypeError: unsupported operand type(s) for +: 'int' and 'str'", "ValueError: invalid literal for int() with base 10: 'currentname'", "KeyError: 'option3'", "IndexError: list index out of range", "AttributeError: 'list' object has no attribute 'appendx'"]

    funnyerrors = ["TypeError: It seems you're trying to perform magic with words! Unfortunately, Python isn't fluent in spellcasting. Please use numbers for multiplication spells.", "IndexError: Oops! You've ventured into the land of the lost indices. Looks like you need a map. Be careful next time, the index monsters can be tricky!", "FileNotFoundError: The file you're looking for seems to have taken a vacation without leaving a note. Please make sure it didn't sneak off to a tropical island. In the meantime, create a new file and give it a stern talking-to.", "SyntaxError: Oh no, the syntax gremlins have been at it again! Your code is speaking in a language Python doesn't understand. Perhaps it's trying to communicate with dolphins? Stick to Pythonic dialects, please.", "KeyError: Uh-oh! You've stumbled upon the legendary lost key of Pythonia. Sadly, it's nowhere to be found in this dictionary. Maybe it's on a quest? Better luck next time, and keep an eye out for adventurous keys."]

    funnyvars = ['unicorn_num', 'bananas', 'burgers_eaten', 'i_dont_know', 'flyingPig', 'lasagna_layers', 'michael_jackson', 'chocolate_rain', 'toiletPaper_Length', 'spiderman_weblength', 'pizza_time', 'iwillnamethisvariablelater', 'starbucks_coffee', 'elonmusk', 'gummybearxd', 'underwaterbasketweaving_level', 'newyorkuniversity', 'minecraft', 'jellybeans', 'joe_biden', 'chucknorris', 'bobby_shmurda']

    funnyfuncnames = ['calculateMyAgeInDogYears', 'findMeaningOfLife', 'orderPizzaDelivery', 'transformIntoAPumpkin', 'playAirGuitar', 'confuseCats', 'predictFuture', 'brewMagicPotion', 'danceLikeNoOneIsWatching', 'summonAliens', 'createUniverse', 'teleportToMars', 'countSheepUntilSleep', 'speakInDolphin', 'calculateIdealPizzaSize', 'writeLoveLetterToCode', 'playInvisiblePiano', 'becomeSuperhero']

    adjusted_numlines = (numlines - 4)//2
    
    if is_silly == False:
        pth = random.choice(paths)

        rnum = random.randint(1, 999)

        print("Traceback (most recent call last):")
        print(f"  File \"{pth}\", line {rnum}, in <module>")

        
        for i in range(0, adjusted_numlines):


                 vname = random.choice(varnames)

                 vname2 = random.choice(varnames)

                 fname = random.choice(func_names)

                 pth = random.choice(paths)

                 rnum = random.randint(1, 999)

                 print(f"    {vname} = {fname}({vname2})")
                 print(f"  File \"{pth}\", line {rnum}, in {fname}")
                 
        vname = random.choice(varnames)
        fname = random.choice(func_names)
        vname2 = random.choice(varnames)
        print(f"    {vname} = {fname}({vname2})")
        print(random.choice(errors))


    #if silly is True we just choose variables from the silly lists
    elif is_silly == True:
        pth = random.choice(paths)

        rnum = random.randint(1, 999)

        print("Traceback (most recent call last):")
        print(f"  File \"{pth}\", line {rnum}, in <module>")
        for i in range(0, adjusted_numlines):


                 vname = random.choice(funnyvars)

                 vname2 = random.choice(funnyvars)

                 fname = random.choice(funnyfuncnames)

                 pth = random.choice(paths)

                 rnum = random.randint(1, 999)

                 print(f"    {vname} = {fname}({vname2})")
                 print(f"  File \"{pth}\", line {rnum}, in {fname}")

        vname = random.choice(funnyvars)
        fname = random.choice(funnyfuncnames)
        vname2 = random.choice(funnyvars)
        print(f"    {vname} = {fname}({vname2})")

        print(random.choice(errors))
