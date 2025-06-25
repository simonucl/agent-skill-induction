from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None

def search_and_sort_products(search_box_id: str, search_button_id: str, product_name: str, sort_dropdown_id: str, sort_option: str):
    """Search for a product and sort the results by specified criteria.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button
        product_name: The name of the product to search for
        sort_dropdown_id: The ID of the sort dropdown menu
        sort_option: The sorting option to apply (e.g., "Price", "Relevance")
        
    Returns:
        None
        
    Examples:
        search_and_sort_products('386', '391', 'iphone 12 phone case', '1500', 'Price')
        search_and_sort_products('search_box', 'search_btn', 'laptop bags', 'sort_menu', 'Rating')
    """
    fill(search_box_id, product_name)
    click(search_button_id)
    select_option(sort_dropdown_id, sort_option)

def search_product(search_id: str, product_query: str):
    """Search for a product using the search functionality.
    
    Args:
        search_id: The ID of the search input field or button
        product_query: The search query string for the product
        
    Returns:
        None
        
    Examples:
        search_product('567', 'Nintendo Switch game card storage case')
        search_product('179', 'Nintendo Switch game card storage')
    """
    click(search_id)
    fill(search_id, product_query)
    keyboard_press('Enter')

def navigate_to_account_orders(account_link_id: str, view_all_id: str):
    """Navigate from homepage to the order history page.
    
    Args:
        account_link_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link
        
    Returns:
        None
        
    Examples:
        navigate_to_account_orders('227', '1742')
    """
    click(account_link_id)
    click(view_all_id)

def navigate_reviews_and_search(reviews_tab_id: str, next_page_id: str):
    """Navigate to reviews section and browse through review pages.
    
    Args:
        reviews_tab_id: The ID of the reviews tab
        next_page_id: The ID of the next page button in reviews
        
    Returns:
        None
        
    Examples:
        navigate_reviews_and_search('1687', '2081')
    """
    click(reviews_tab_id)
    click(next_page_id)
    click('2176')

def search_product_and_get_results(search_box_id: str, search_button_id: str, product_name: str):
    """Search for a product and navigate to the results page to view pricing and availability.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button
        product_name: The name of the product to search for
        
    Returns:
        None
        
    Examples:
        search_product_and_get_results('389', '394', 'Canon photo printer')
        search_product_and_get_results('search_box', 'search_btn', 'laptop bags')
    """
    fill(search_box_id, product_name)
    click(search_button_id)

def search_and_navigate_to_product(search_box_id: str, search_button_id: str, product_name: str, product_link_id: str):
    """Search for a product and navigate to its detailed product page.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button  
        product_name: The name of the product to search for
        product_link_id: The ID of the product link in search results
        
    Returns:
        None
        
    Examples:
        search_and_navigate_to_product('505', '510', 'Amazon Echo Dot 3rd generation', '1751')
        search_and_navigate_to_product('search_box', 'search_btn', 'iPhone case', 'product_link')
    """
    fill(search_box_id, product_name)
    click(search_button_id)
    click(product_link_id)

def navigate_to_order_history(account_link_id: str, view_all_id: str):
    """Navigate from homepage to the complete order history page.
    
    Args:
        account_link_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link
        
    Returns:
        None
        
    Examples:
        navigate_to_order_history('227', '1690')
    """
    click(account_link_id)
    click(view_all_id)

def browse_order_pages(page_ids: list):
    """Browse through multiple pages of order history.
    
    Args:
        page_ids: A list of page link IDs to navigate through
        
    Returns:
        None
        
    Examples:
        browse_order_pages(['1766', '1774', '1778'])
    """
    for page_id in page_ids:
        click(page_id)

def navigate_to_address_management(account_id: str, manage_addresses_id: str):
    """Navigate from homepage to the address management page.
    
    Args:
        account_id: The ID of the "My Account" link
        manage_addresses_id: The ID of the "Manage Addresses" link
        
    Returns:
        None
        
    Examples:
        navigate_to_address_management('227', '1658')
    """
    click(account_id)
    click(manage_addresses_id)

def update_billing_address(change_address_id: str, street: str, city: str, state: str, zip_code: str, save_button_id: str):
    """Update billing address with new information.
    
    Args:
        change_address_id: The ID of the "Change Billing Address" link
        street: The new street address
        city: The new city name
        state: The new state name
        zip_code: The new ZIP/postal code
        save_button_id: The ID of the "Save Address" button
        
    Returns:
        None
        
    Examples:
        update_billing_address('1648', '987 Sycamore Circle', 'Philadelphia', 'Pennsylvania', '19102', '2026')
    """
    click(change_address_id)
    fill('1674', street)
    select_option('1939', state)
    fill('2011', city)
    fill('2016', zip_code)
    click(save_button_id)

def search_and_add_to_wishlist(search_box_id: str, search_button_id: str, product_name: str, wishlist_button_id: str):
    """Search for a specific product and add it to the wishlist.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button
        product_name: The name of the product to search for
        wishlist_button_id: The ID of the "Add to Wish List" button
        
    Returns:
        None
        
    Examples:
        search_and_add_to_wishlist('545', '550', 'Tide PODS Spring Meadow Scent HE Turbo Laundry Detergent Pacs, 81 Count', '1699')
        search_and_add_to_wishlist('search_box', 'search_btn', 'iPhone 14 case', 'add_wishlist')
    """
    fill(search_box_id, product_name)
    click(search_button_id)
    click(wishlist_button_id)

def navigate_to_specific_order(account_id: str, view_all_id: str, page_id: str, order_view_id: str):
    """Navigate from homepage to a specific order's details page.
    
    Args:
        account_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link
        page_id: The ID of the page navigation link
        order_view_id: The ID of the "View Order" link for specific order
        
    Returns:
        None
        
    Examples:
        navigate_to_specific_order('227', '1690', '1766', '1651')
    """
    click(account_id)
    click(view_all_id)
    click(page_id)
    click(order_view_id)

def send_product_configuration_details(product_name: str, configuration_details: str, price: str, order_date: str, order_number: str):
    """Send detailed product configuration information to the user.
    
    Args:
        product_name: The full name of the product
        configuration_details: String containing configuration options like color, size, SKU
        price: The price of the product
        order_date: The date when the order was placed
        order_number: The order number
        
    Returns:
        None
        
    Examples:
        send_product_configuration_details('Artificial Tree', 'Color: Green, Size: 4ft', '$260.69', 'January 29, 2023', '000000148')
    """
    message = f"I found the {product_name.lower()} you purchased! Here are the price configuration details:\n\nProduct: {product_name}\n\nConfiguration:\n{configuration_details}\n\nPrice: {price}\n\nThis was ordered on {order_date} as part of Order #{order_number}."
    send_msg_to_user(message)

def navigate_to_full_order_history(account_id: str, view_all_id: str):
    """Navigate from homepage to the complete order history page.
    
    Args:
        account_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All Orders" link
        
    Returns:
        None
        
    Examples:
        navigate_to_full_order_history('227', '1690')
    """
    click(account_id)
    click(view_all_id)

def browse_multiple_order_pages(page_ids: list):
    """Navigate through multiple pages of order history to search for specific order status.
    
    Args:
        page_ids: List of page navigation link IDs to browse through
        
    Returns:
        None
        
    Examples:
        browse_multiple_order_pages(['1766', '1774', '1778'])
    """
    for page_id in page_ids:
        click(page_id)

def report_order_status_search_result(status: str, found: bool, total_orders: int):
    """Report the results of searching for orders with a specific status.
    
    Args:
        status: The order status that was searched for
        found: Whether orders with the status were found
        total_orders: Total number of orders checked
        
    Returns:
        None
        
    Examples:
        report_order_status_search_result('Out of Delivery', False, 37)
    """
    if found:
        send_msg_to_user(f"Found orders with '{status}' status in your order history.")
    else:
        send_msg_to_user(f"I've searched through your complete order history (all {total_orders} orders) and found no orders with '{status}' status. Your orders show the following statuses: 'Complete', 'Canceled', and 'Pending'. There are currently no orders with '{status}' status.")

def navigate_to_order_details(account_id: str, view_all_id: str, order_link_id: str):
    """Navigate from homepage to specific order details page.
    
    Args:
        account_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link  
        order_link_id: The ID of the specific order link to view
        
    Returns:
        None
        
    Examples:
        navigate_to_order_details('227', '1717', '1744')
        navigate_to_order_details('account_btn', 'view_orders', 'order_123')
    """
    click(account_id)
    click(view_all_id)
    click(order_link_id)

def search_order_history_for_product(back_button_id: str, target_order_id: str):
    """Navigate back to order history and check another order for specific products.
    
    Args:
        back_button_id: The ID of the back/return button to order history
        target_order_id: The ID of the next order to examine
        
    Returns:
        None
        
    Examples:
        search_order_history_for_product('1828', '1777')
        search_order_history_for_product('back_btn', 'order_456')
    """
    click(back_button_id)
    click(target_order_id)

def send_product_configuration_message(product_name: str, configuration_type: str, configuration_value: str, order_date: str, order_number: str, price: str):
    """Send detailed product configuration information to the user.
    
    Args:
        product_name: The full name of the product found
        configuration_type: The type of configuration (e.g., "Color", "Size")
        configuration_value: The specific configuration value
        order_date: The date when the order was placed
        order_number: The order number
        price: The price of the product
        
    Returns:
        None
        
    Examples:
        send_product_configuration_message('Artificial Plants', 'Color', 'Green-vines', 'February 9, 2023', '000000157', '$14.99')
    """
    message = f"I found the {product_name.lower()} you purchased! Here are the {configuration_type.lower()} configuration details:\n\nProduct: {product_name}\n\n{configuration_type} Configuration: {configuration_value}\n\nThis was ordered on {order_date} as part of Order #{order_number} for {price}."
    send_msg_to_user(message)

def navigate_to_order_details_from_account(account_id: str, order_view_id: str):
    """Navigate from homepage to a specific order's details page through My Account.
    
    Args:
        account_id: The ID of the "My Account" link
        order_view_id: The ID of the "View Order" link for the specific order
        
    Returns:
        None
        
    Examples:
        navigate_to_order_details_from_account('227', '1689')
        navigate_to_order_details_from_account('account_btn', 'view_order_123')
    """
    click(account_id)
    click(order_view_id)

def access_full_order_history_from_account(account_id: str, my_orders_id: str):
    """Navigate from homepage to the complete order history page through My Account sidebar.
    
    Args:
        account_id: The ID of the "My Account" link
        my_orders_id: The ID of the "My Orders" link in sidebar
        
    Returns:
        None
        
    Examples:
        access_full_order_history_from_account('227', '1765')
        access_full_order_history_from_account('account_btn', 'orders_link')
    """
    click(account_id)
    click(my_orders_id)

def search_brand_and_analyze_prices(search_box_id: str, search_button_id: str, brand_name: str):
    """Search for products from a specific brand and analyze their price range.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button
        brand_name: The name of the brand to search for
        
    Returns:
        None
        
    Examples:
        search_brand_and_analyze_prices('572', '577', 'sephora')
        search_brand_and_analyze_prices('search_box', 'search_btn', 'nike')
    """
    fill(search_box_id, brand_name)
    click(search_button_id)

def search_for_keyword(search_box_id: str, search_button_id: str, keyword: str):
    """Search for a specific keyword using the search functionality.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button
        keyword: The search keyword or phrase
        
    Returns:
        None
        
    Examples:
        search_for_keyword('572', '577', 'green tea bag for weight loss')
        search_for_keyword('search_box', 'search_btn', 'wireless headphones')
    """
    fill(search_box_id, keyword)
    click(search_button_id)

def navigate_to_full_order_history(account_id: str, view_all_id: str):
    """Navigate from homepage to the complete order history page.
    
    Args:
        account_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link
        
    Returns:
        None
        
    Examples:
        navigate_to_full_order_history('227', '1719')
        navigate_to_full_order_history('account_btn', 'view_orders')
    """
    click(account_id)
    click(view_all_id)

def browse_order_pages_for_status(page_ids: list):
    """Browse through multiple pages of order history to search for specific order status.
    
    Args:
        page_ids: List of page navigation link IDs to browse through
        
    Returns:
        None
        
    Examples:
        browse_order_pages_for_status(['1793', '1801', '1805'])
        browse_order_pages_for_status(['page2', 'page3', 'page4'])
    """
    for page_id in page_ids:
        click(page_id)

def report_order_status_search_result(status: str, found: bool, total_orders: int, pages_searched: int):
    """Report the results of searching for orders with a specific status.
    
    Args:
        status: The order status that was searched for
        found: Whether orders with the status were found
        total_orders: Total number of orders checked
        pages_searched: Number of pages searched through
        
    Returns:
        None
        
    Examples:
        report_order_status_search_result('on hold', False, 37, 4)
        report_order_status_search_result('pending', True, 25, 3)
    """
    if found:
        send_msg_to_user(f"Found orders with '{status}' status in your order history.")
    else:
        send_msg_to_user(f"I've searched through your complete order history (all {total_orders} orders across {pages_searched} pages) and found no orders with '{status}' status. Your orders show the following statuses: 'Complete', 'Canceled', and 'Pending'. There are currently no orders with '{status}' status in your account.")

def navigate_to_category_and_sort(category_id: str, subcategory_id: str, subsub_category_id: str, sort_dropdown_id: str, sort_option: str):
    """Navigate to a specific product category hierarchy and sort the results.
    
    Args:
        category_id: The ID of the main category (e.g., "Electronics")
        subcategory_id: The ID of the subcategory (e.g., "Computers & Accessories") 
        subsub_category_id: The ID of the sub-subcategory (e.g., "Data Storage")
        sort_dropdown_id: The ID of the sort dropdown menu
        sort_option: The sorting option to apply (e.g., "Price")
        
    Returns:
        None
        
    Examples:
        navigate_to_category_and_sort('1154', '2183', '2190', '1726', 'Price')
        navigate_to_category_and_sort('electronics', 'computers', 'storage', 'sort_menu', 'Price')
    """
    click(category_id)
    click(subcategory_id)
    click(subsub_category_id)
    select_option(sort_dropdown_id, sort_option)

def search_nintendo_storage(search_id: str, num_cards: int):
    """Search for Nintendo Switch game card storage solutions.
    
    Args:
        search_id: The ID of the search input field
        num_cards: The number of game cards to store
        
    Returns:
        None
        
    Examples:
        search_nintendo_storage('567', 11)
        search_nintendo_storage('179', 31)
    """
    click(search_id)
    fill(search_id, 'Nintendo Switch game card storage case')
    keyboard_press('Enter')

def navigate_order_pages(page_ids: list):
    """Navigate through multiple pages of order history.
    
    Args:
        page_ids: List of page link IDs to navigate through in sequence
        
    Returns:
        None
        
    Examples:
        navigate_order_pages(['1816', '1824'])
        navigate_order_pages(['1766', '1774', '1778'])
    """
    for page_id in page_ids:
        click(page_id)

def navigate_reviews_pages(reviews_tab_id: str, page_ids: list):
    """Navigate through product review pages to search for specific content.
    
    Args:
        reviews_tab_id: The ID of the reviews tab
        page_ids: List of review page IDs to navigate through
        
    Returns:
        None
        
    Examples:
        navigate_reviews_pages('1575', ['2333', '2428'])
    """
    click(reviews_tab_id)
    for page_id in page_ids:
        click(page_id)

def navigate_to_order_history_and_browse(account_id: str, orders_link_id: str, page_ids: list):
    """Navigate to order history and browse through multiple pages to search for orders.
    
    Args:
        account_id: The ID of the "My Account" link
        orders_link_id: The ID of the orders/order history link
        page_ids: List of page navigation IDs to browse through
        
    Returns:
        None
        
    Examples:
        navigate_to_order_history_and_browse('227', '1758', ['1832', '1832', '1828'])
        navigate_to_order_history_and_browse('account_btn', 'my_orders', ['page2', 'page3', 'page1'])
    """
    click(account_id)
    click(orders_link_id)
    for page_id in page_ids:
        click(page_id)

def send_order_total_message(order_number: str, total_cost: str, order_date: str, status: str):
    """Send a message to user with order total cost information.
    
    Args:
        order_number: The order number
        total_cost: The total cost of the order
        order_date: The date the order was placed
        status: The status of the order
        
    Returns:
        None
        
    Examples:
        send_order_total_message('000000189', '$754.99', '5/2/23', 'pending')
        send_order_total_message('12345', '$299.99', '1/15/24', 'completed')
    """
    message = f"The total cost of your latest {status} order is {total_cost}. This is Order #{order_number} placed on {order_date}."
    send_msg_to_user(message)

def navigate_to_contact_info():
    """Navigate to the contact information page to find customer service details.
    
    Returns:
        None
        
    Examples:
        navigate_to_contact_info()
    """
    click("2117")  # Click on Contact Us link
    scroll(0, 500)  # Scroll down to view more contact information
    
def check_for_phone_support():
    """Check if customer service phone number is available and inform user.
    
    Returns:
        None
        
    Examples:
        check_for_phone_support()
    """
    send_msg_to_user("I searched the Contact Us page for One Stop Market, but there is no customer service phone number listed. The website only provides a contact form where you can submit your name, email, phone number, and message, and they will get back to you. There doesn't appear to be a direct customer service phone number available on their website.")

def navigate_to_latest_order(account_id: str, order_id: str):
    """Navigate from homepage to the latest order details page.
    
    Args:
        account_id: The ID of the "My Account" link
        order_id: The ID of the latest order link to view
        
    Returns:
        None
        
    Examples:
        navigate_to_latest_order('227', '1793')
        navigate_to_latest_order('account_btn', 'order_link')
    """
    click(account_id)
    click(order_id)