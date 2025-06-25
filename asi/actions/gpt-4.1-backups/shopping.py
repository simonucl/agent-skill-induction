from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None


def access_order_details(account_id: str, order_view_id: str):
    """
    Navigate to account page and view a specific order's details.

    Args:
        account_id: The ID of the "My Account" link.
        order_view_id: The ID to click and view the specific order.

    Returns:
        None

    Examples:
        access_order_details('227', '1553')
    """
    click(account_id)
    click(order_view_id)

def open_reviews_and_next_page(reviews_tab_id: str, next_page_id: str):
    """
    Opens the reviews tab and navigates to the next review page.
    
    Args:
        reviews_tab_id: The element ID for the reviews tab.
        next_page_id: The element ID for the next page of reviews.
    
    Returns:
        None
    
    Examples:
        open_reviews_and_next_page('1688', '2081')
    
    """
    click(reviews_tab_id)
    click(next_page_id)

def subscribe_newsletter(email_field_id: str, subscribe_button_id: str, email_address: str):
    """
    Subscribes to a newsletter by filling the email input and clicking the subscribe button.

    Args:
        email_field_id: The element ID of the email input textbox.
        subscribe_button_id: The element ID of the subscribe button.
        email_address: The email address to use for subscribing.

    Returns:
        None

    Examples:
        subscribe_newsletter('1964', '1966', 'sample@email.com')
    """
    fill(email_field_id, email_address)
    click(subscribe_button_id)

def search_and_add_to_wishlist(category_id: str, subcategory_id: str, advanced_search_id: str, name_field_id: str, search_button_id: str, product_name: str, wishlist_button_id: str):
    """
    Navigates through categories, performs an advanced product search, and adds the first relevant result to the wish list.

    Args:
        category_id: The ID of the main category to click (e.g., 'Office Products').
        subcategory_id: The ID of the subcategory to filter products (e.g., 'Office Furniture & Lighting').
        advanced_search_id: The ID for the advanced search feature.
        name_field_id: The element ID for the product name input field.
        search_button_id: The ID for the search/submit button.
        product_name: The name of the product to search for.
        wishlist_button_id: The ID of the "Add to Wish List" button for the relevant product.

    Returns:
        None

    Examples:
        search_and_add_to_wishlist('836', '1925', '392', '1488', '1520', 'white computer desk', '1542')
    """
    click(category_id)
    click(subcategory_id)
    click(advanced_search_id)
    fill(name_field_id, product_name)
    click(search_button_id)
    click(wishlist_button_id)

def search_and_open_product(search_field_id: str, search_button_id: str, product_name: str, product_link_id: str):
    """
    Searches for a product using a search field, clicks the search button, and then opens the product details page.

    Args:
        search_field_id: The element ID of the search input field.
        search_button_id: The element ID of the search button.
        product_name: The name of the product to search for.
        product_link_id: The ID of the anchor/link to the target product.

    Returns:
        None

    Examples:
        search_and_open_product('505', '510', 'Amazon Echo Dot 3rd generation', '1382')
    """
    fill(search_field_id, product_name)
    click(search_button_id)
    click(product_link_id)
    

def open_reviews_tab(reviews_tab_id: str):
    """
    Opens the reviews tab for a product.

    Args:
        reviews_tab_id: The element ID for the "Reviews" tab.

    Returns:
        None

    Examples:
        open_reviews_tab('1751')
    """
    click(reviews_tab_id)

def search_and_sort_listings(search_field_id: str, search_button_id: str, search_query: str, sort_dropdown_id: str, sort_option: str, sort_direction_button_id: str):
    """
    Searches for a product/listings, selects a sort criterion, and sorts in the desired direction.

    Args:
        search_field_id: The element ID of the search input field.
        search_button_id: The element ID of the search/submit button.
        search_query: The string to use for the search (e.g., "chairs").
        sort_dropdown_id: The element ID of the sort dropdown.
        sort_option: The option to select in the sort dropdown (e.g., "Price").
        sort_direction_button_id: The ID of the button/link to set the sort direction (e.g., ascending/descending).

    Returns:
        None

    Examples:
        search_and_sort_listings('505', '510', 'chairs', '1378', 'Price', '1624')
    """
    fill(search_field_id, search_query)
    click(search_button_id)
    select_option(sort_dropdown_id, sort_option)
    click(sort_direction_button_id)

def search_and_add_to_wishlist_simple(search_field_id: str, search_button_id: str, product_name: str, wishlist_button_id: str):
    """
    Searches for a product and adds it to the wish list from the search results.

    Args:
        search_field_id: The ID of the search input field.
        search_button_id: The ID of the search button.
        product_name: The name of the product to search for.
        wishlist_button_id: The ID of the "Add to Wish List" button for the relevant product.

    Returns:
        None

    Examples:
        search_and_add_to_wishlist_simple('505', '510', 'Tide PODS Spring Meadow Scent', '1659')
    """
    fill(search_field_id, product_name)
    click(search_button_id)
    click(wishlist_button_id)

def navigate_order_history(account_id: str, view_all_id: str, *page_ids: str):
    """
    Navigate to the order history, optionally through several pagination steps.

    Args:
        account_id: The ID for the "My Account" link.
        view_all_id: The ID for the "View All" link to see all orders.
        *page_ids: Optional sequence of pagination IDs to reach an older order.

    Returns:
        None

    Examples:
        navigate_order_history('227', '1650', '1726')
    """
    click(account_id)
    click(view_all_id)
    for pid in page_ids:
        click(pid)

def hover_and_browse_category(main_menu_id: str, submenu_id: str, category_id: str):
    """
    Hover over the main menu and submenu to access and click a specific category.

    Args:
        main_menu_id: The element ID of the main menu (e.g., 'Home & Kitchen').
        submenu_id: The element ID of the submenu (e.g., 'Storage & Organization').
        category_id: The element ID of the final category to browse (e.g., 'Racks, Shelves & Drawers').

    Returns:
        None

    Examples:
        hover_and_browse_category('827', '878', '889')
    """
    hover(main_menu_id)
    hover(submenu_id)
    click(category_id)


def paginate_through_category(*pagination_ids: str):
    """
    Paginate through a category by clicking page or next buttons provided as IDs.

    Args:
        *pagination_ids: Variable number of pagination element IDs (e.g., '2060', '2053', etc.).

    Returns:
        None

    Examples:
        paginate_through_category('2060', '2053', '2012')
    """
    for pid in pagination_ids:
        click(pid)

def check_all_orders(account_id: str, view_all_id: str, pagination_ids: list[str]):
    """
    Navigate through all paginated order history pages to check for a specific order status.

    Args:
        account_id: The ID for the "My Account" link.
        view_all_id: The ID for the "View All" link to see all orders.
        pagination_ids: List of pagination element IDs to visit further order pages (e.g., ['1726', '1734', '1738']).

    Returns:
        None

    Examples:
        check_all_orders('227', '1650', ['1726', '1734', '1738'])
    """
    click(account_id)
    click(view_all_id)
    for pid in pagination_ids:
        click(pid)

def browse_full_order_history(account_id: str, view_all_id: str, *pagination_ids: str):
    """
    Navigates to the full order history, traversing specified pagination buttons to check all pages.

    Args:
        account_id: The ID for the "My Account" link on the navigation/menu.
        view_all_id: The ID for the "View All" link next to Recent Orders.
        *pagination_ids: Optional element IDs representing pagination buttons for additional order history (e.g., next/previous page).

    Returns:
        None

    Examples:
        browse_full_order_history('227', '1650', '1726', '1722')
    """
    click(account_id)
    click(view_all_id)
    for pid in pagination_ids:
        click(pid)

def navigate_order_history_with_pagination(account_id: str, view_all_id: str, *page_ids: str):
    """
    Navigates from the account page to the full order history with optional pagination.

    Args:
        account_id: The ID of the "My Account" link.
        view_all_id: The ID of the "View All" orders link.
        *page_ids: Variable length sequence of page IDs to paginate through order history.

    Returns:
        None

    Examples:
        navigate_order_history_with_pagination('227', '1677', '1753')
        navigate_order_history_with_pagination('227', '1677')
    """
    click(account_id)
    click(view_all_id)
    for pid in page_ids:
        click(pid)

def navigate_full_order_history(account_id: str, view_all_id: str):
    """
    Navigates from the homepage to the full order history list.

    Args:
        account_id: The element ID for the "My Account" link.
        view_all_id: The element ID for the "View All" link to access all orders.

    Returns:
        None

    Examples:
        navigate_full_order_history('227', '1677')
    """
    click(account_id)
    click(view_all_id)

def scroll_through_order_history(scroll_steps: int, scroll_amount: int = 500):
    """
    Scrolls through the order history by a specified number of steps.

    Args:
        scroll_steps: Number of times to scroll down the order page.
        scroll_amount: The pixel amount to scroll per step (default: 500).

    Returns:
        None

    Examples:
        scroll_through_order_history(3)
    """
    for _ in range(scroll_steps):
        scroll(0, scroll_amount)

def open_full_order_history_with_pagination(account_id: str, view_all_id: str, pagination_ids: list[str]):
    """
    Navigates to the full order history and traverses multiple pagination steps.

    Args:
        account_id: The ID for the "My Account" link.
        view_all_id: The ID for the "View All" orders link.
        pagination_ids: List of pagination element IDs to visit additional order history pages.

    Returns:
        None

    Examples:
        open_full_order_history_with_pagination('227', '1420', ['1506', '1502', '1510'])
    """
    click(account_id)
    click(view_all_id)
    for pid in pagination_ids:
        click(pid)

def search_and_sort_products(search_field_id: str, search_button_id: str, search_query: str, sort_dropdown_id: str, sort_option: str, sort_direction_button_id: str):
    """
    Searches for products, sorts the search results by a given criterion and direction.

    Args:
        search_field_id: The element ID of the search input field.
        search_button_id: The element ID of the search/submit button.
        search_query: The string to use for the product search (e.g., "1TB SSD").
        sort_dropdown_id: The element ID of the sort dropdown.
        sort_option: The option to select in the sort dropdown (e.g., "Price").
        sort_direction_button_id: The ID of the button/link to set the sort direction (e.g., ascending/descending).

    Returns:
        None

    Examples:
        search_and_sort_products('437', '442', "1TB SSD", '1552', 'Price', '1556')
    """
    fill(search_field_id, search_query)
    click(search_button_id)
    select_option(sort_dropdown_id, sort_option)
    click(sort_direction_button_id)

def view_order_history_and_order(account_id: str, view_all_id: str, order_view_id: str):
    """
    Navigates to the order history and opens a particular order detail page.

    Args:
        account_id: Element ID for "My Account" link.
        view_all_id: Element ID for "View All" (order history or recent orders).
        order_view_id: Element ID for the "View Order" link of a specific order.

    Returns:
        None

    Examples:
        view_order_history_and_order('227', '1584', '1543')
    """
    click(account_id)
    click(view_all_id)
    click(order_view_id)

def scroll_through_orders(scroll_steps: int, scroll_amount: int = 500):
    """
    Scrolls through the order history page for the specified number of steps.

    Args:
        scroll_steps: How many times to scroll (each scroll moves by scroll_amount).
        scroll_amount: The vertical pixels to scroll per step (default 500).

    Returns:
        None

    Examples:
        scroll_through_orders(3)
    """
    for _ in range(scroll_steps):
        scroll(0, scroll_amount)

def prepare_contact_form_refund(account_id: str, view_all_orders_id: str, contact_us_id: str, message_field_id: str, message_text: str):
    """
    Navigates from the account page and order history to the "Contact Us" form and drafts the refund message.

    Args:
        account_id: The ID for the "My Account" link.
        view_all_orders_id: The ID for the "View All" orders link.
        contact_us_id: The ID for the "Contact Us" form link/button.
        message_field_id: The ID of the message input field in the contact form.
        message_text: The refund message to fill into the contact form.

    Returns:
        None

    Examples:
        prepare_contact_form_refund('227', '1584', '1882', '1547', 'Order ID: 000000166\nReason: ...')
    """
    click(account_id)
    click(view_all_orders_id)
    click(contact_us_id)
    fill(message_field_id, message_text)

def open_reviews_tab_and_send_criticisms(reviews_tab_id: str, criticisms: list[str], product_name: str = ""):
    """
    Opens the Reviews tab for a product and sends the relevant criticisms to the user.

    Args:
        reviews_tab_id: The element ID for the reviews tab or button.
        criticisms: A list of strings, each being a main criticism extracted from reviews.
        product_name: Optional. The name of the product for formatting the message.

    Returns:
        None

    Examples:
        open_reviews_tab_and_send_criticisms('2070', [
            "The 39 was too small. They are so cute! I am afraid the 40 will be too big.",
            "I was very sad when the shoe rubbed up against my baby toe. I had to return them because I knew in time it would tear up my feet. Everything was perfect except the fit.",
            "The problem is that the strap is made of some really stiff leather and is painful to my heel. The front is also uncomfortably tight."
        ], "Sandgrens Swedish Handmade Wooden Clog Sandal | Copenhagen")
    """
    click(reviews_tab_id)
    msg = "The main criticisms"
    if product_name:
        msg += f" of the {product_name}"
    msg += " are:\n"
    for i, c in enumerate(criticisms, 1):
        msg += f"{i}. '{c}'\n"
    send_msg_to_user(msg.strip())

def navigate_to_full_order_history(account_id: str, view_all_orders_id: str):
    """
    Navigates from the main page to the full order history listing.

    Args:
        account_id: The ID of the "My Account" link.
        view_all_orders_id: The ID of the "View All" link to access all orders.

    Returns:
        None

    Examples:
        navigate_to_full_order_history('227', '1691')
    """
    click(account_id)
    click(view_all_orders_id)

def open_latest_order(account_id: str, latest_order_id: str):
    """
    Navigates to the account section and opens the details page for the latest order.

    Args:
        account_id: The ID for the "My Account" link.
        latest_order_id: The ID for the "View Order" button/link of the latest order.

    Returns:
        None

    Examples:
        open_latest_order('227', '1714')
    """
    click(account_id)
    click(latest_order_id)

def search_brand_products(search_field_id: str, search_button_id: str, brand_name: str):
    """
    Searches for products by a given brand name.

    Args:
        search_field_id: The ID of the search input field.
        search_button_id: The ID of the search button.
        brand_name: The brand name to search for.

    Returns:
        None

    Examples:
        search_brand_products('635', '640', 'EYZUTAK')
    """
    fill(search_field_id, brand_name)
    click(search_button_id)

def navigate_order_history_with_pages(account_id: str, view_all_id: str, page_ids: list[str]):
    """
    Navigates from the main account page to the order history, traversing through multiple paginated pages as needed.

    Args:
        account_id: The element ID for the "My Account" link (e.g., '227').
        view_all_id: The element ID for the "View All" orders link (e.g., '1782').
        page_ids: List of page element IDs (e.g., ['1856', '1864', '1868']) for each additional order history pagination step.

    Returns:
        None

    Examples:
        navigate_order_history_with_pages('227', '1782', ['1856', '1864', '1868'])
    """
    click(account_id)
    click(view_all_id)
    for pid in page_ids:
        click(pid)

def navigate_order_history_with_multiple_pages(account_id: str, view_all_id: str, page_ids: list[str]):
    """
    Navigates from the main account page to the order history, traversing through multiple pagination pages as needed.

    Args:
        account_id: The element ID for the "My Account" link (e.g., '227').
        view_all_id: The element ID for the "View All" orders link (e.g., '1782').
        page_ids: List of page element IDs (e.g., ['1856', '1860', '1868']) for each additional order history pagination step.

    Returns:
        None

    Examples:
        navigate_order_history_with_multiple_pages('227', '1782', ['1856', '1860', '1868'])
    """
    click(account_id)
    click(view_all_id)
    for pid in page_ids:
        click(pid)

def view_order_details_and_send_refund(order_id: str, refund_message: str):
    """
    View a specific order's details and send the refund summary to the user.

    Args:
        order_id: The element ID of the link/button to see the order details (e.g., '1807').
        refund_message: The message explaining the expected refund amount.

    Returns:
        None

    Examples:
        view_order_details_and_send_refund('1807', 'You should expect a refund of $77.90 ...')
    """
    click(order_id)
    send_msg_to_user(refund_message)

def view_orders_across_pages(account_id: str, view_all_id: str, *pagination_ids: str):
    """
    Navigates to the full order history page, traversing additional pages as needed.

    Args:
        account_id: The ID for the "My Account" link.
        view_all_id: The ID for the "View All" orders link.
        *pagination_ids: Variable number of element IDs for pagination (e.g., for Page 2, Page 3, etc.).

    Returns:
        None

    Examples:
        view_orders_across_pages('227', '1782', '1856')
        view_orders_across_pages('227', '1782')
    """
    click(account_id)
    click(view_all_id)
    for pid in pagination_ids:
        click(pid)

def search_for_product(search_field_id: str, search_button_id: str, product_name: str):
    """
    Fill the search bar, submit the search, and show product results for a keyword.

    Args:
        search_field_id: The element ID of the search input field.
        search_button_id: The element ID of the search/submit button.
        product_name: The name or keyword(s) to search for.

    Returns:
        None

    Examples:
        search_for_product('637', '642', 'Nike slide slippers')
    """
    fill(search_field_id, product_name)
    click(search_button_id)

def open_full_order_history_with_pages(account_id: str, view_all_id: str, page_ids: list[str]):
    """
    Navigates through the account and order history, traversing paginated pages as specified.

    Args:
        account_id: The ID of the "My Account" link.
        view_all_id: The ID for the "View All" link in Recent Orders.
        page_ids: List of IDs for page navigation (e.g., page 2, 3, 4, ...).

    Returns:
        None

    Examples:
        open_full_order_history_with_pages('227', '1784', ['1858', '1862', '1870'])
    """
    click(account_id)
    click(view_all_id)
    for pid in page_ids:
        click(pid)

def open_order_history_and_paginate(account_id: str, view_all_id: str, *page_ids: str):
    """
    Navigates to the full order history and paginates through the specified pages.

    Args:
        account_id: The ID of the "My Account" link.
        view_all_id: The ID for the "View All" orders link.
        *page_ids: Variable number of page IDs to paginate through order history.

    Returns:
        None

    Examples:
        open_order_history_and_paginate('227', '1784', '1858')
        open_order_history_and_paginate('227', '1784')
    """
    click(account_id)
    click(view_all_id)
    for pid in page_ids:
        click(pid)

def open_full_order_history(account_id: str, view_all_id: str):
    """
    Navigates from the main page to the full order history listing.

    Args:
        account_id: The element ID for the "My Account" link.
        view_all_id: The element ID for the "View All" link to access all orders.

    Returns:
        None

    Examples:
        open_full_order_history('227', '1784')
    """
    click(account_id)
    click(view_all_id)

def draft_refund_message(account_id: str, view_all_orders_id: str, order_id: str, product: str, amount: str):
    """
    Navigates to the account and orders section, then drafts a refund message for the user (does not submit).

    Args:
        account_id: The element ID for the "My Account" link.
        view_all_orders_id: The element ID for the "View All" orders link.
        order_id: The string representing the order ID (e.g., '000000161').
        product: The product to mention in the refund reason.
        amount: The amount requested for refund.

    Returns:
        None

    Examples:
        draft_refund_message('227', '1784', '000000161', 'Bluetooth speaker', '$762.18')
    """
    click(account_id)
    click(view_all_orders_id)
    msg = (
        f"Here is your refund message draft:\n\n"
        f"Order ID: {order_id}\n"
        f"Reason: The {product} I purchased broke after only three days of use.\n"
        f"Amount to refund: {amount}\n\n"
        f"Let me know if you want to proceed or make any changes."
    )
    send_msg_to_user(msg)

def open_full_order_history_and_view_order(account_id: str, view_all_id: str, page_id: str, order_view_id: str):
    """
    Navigates to the full order history, moves to a specified page, and views a specific order.

    Args:
        account_id: The ID for the "My Account" link.
        view_all_id: The ID for the "View All" orders link.
        page_id: The ID for the target pagination button (e.g., "Page 2").
        order_view_id: The ID for the "View Order" link/button for the target order.

    Returns:
        None

    Examples:
        open_full_order_history_and_view_order('227', '1784', '1858', '1754')
    """
    click(account_id)
    click(view_all_id)
    click(page_id)
    click(order_view_id)

def search_for_brand_product(search_field_id: str, search_button_id: str, brand_name: str, product_name: str):
    """
    Searches for a specific product type from a particular brand using the search field and search button.

    Args:
        search_field_id: The element ID of the search input field.
        search_button_id: The ID of the search button.
        brand_name: The brand name to include in the search (e.g., "Anker").
        product_name: The type/keyword of the product to search for (e.g., "charger").

    Returns:
        None

    Examples:
        search_for_brand_product('637', '642', 'Anker', 'charger')
    """
    fill(search_field_id, f"{brand_name} {product_name}")
    click(search_button_id)

def navigate_and_view_order(account_id: str, view_all_id: str, page_id: str, order_view_id: str):
    """
    Navigates to the order history, paginates to the specified page, and opens the specific order.

    Args:
        account_id: Element ID for the "My Account" link.
        view_all_id: Element ID for the "View All" orders/history link.
        page_id: Element ID for the page navigation (e.g., "Page 2").
        order_view_id: Element ID for the specific order's "View Order" link.

    Returns:
        None

    Examples:
        navigate_and_view_order('227', '1784', '1858', '1842')
    """
    click(account_id)
    click(view_all_id)
    click(page_id)
    click(order_view_id)

def open_orders_and_check_orders(account_id: str, view_all_id: str, *order_view_ids: str):
    """
    Navigates to order history, opens the full history, and checks several orders by their view IDs.
    
    Args:
        account_id: The ID for the "My Account" button/link.
        view_all_id: The ID for the "View All" link under orders.
        *order_view_ids: Sequence of IDs for the "View Order" buttons to examine.
        
    Returns:
        None
        
    Examples:
        open_orders_and_check_orders('227', '1784', '1743', '1807')
    """
    click(account_id)
    click(view_all_id)
    for order_view_id in order_view_ids:
        click(order_view_id)

def search_and_add_to_wishlist_simple_with_msg(search_field_id: str, search_button_id: str, product_name: str, wishlist_button_id: str, already_added: bool = False):
    """
    Searches for a product and adds it to the wish list from the search results, then optionally notifies the user if the product is already present.

    Args:
        search_field_id: The ID of the search input field.
        search_button_id: The ID of the search button.
        product_name: The name of the product to search for.
        wishlist_button_id: The ID of the "Add to Wish List" button for the relevant product.
        already_added: If True, sends a message that the product is already in the wish list.

    Returns:
        None

    Examples:
        search_and_add_to_wishlist_simple_with_msg('637', '642', 'HONGJ Hawaiian Beach Outfits Set', '1795', already_added=True)
    """
    fill(search_field_id, product_name)
    click(search_button_id)
    click(wishlist_button_id)
    if already_added:
        send_msg_to_user(f"The product '{product_name}' has already been added to your wish list and is visible in your wish list items.")

def open_latest_order_and_prepare_review(account_id: str, latest_order_id: str) -> None:
    """
    Navigates to the account section and opens the details page for the latest order, typically before leaving a review.

    Args:
        account_id: The ID for the "My Account" link.
        latest_order_id: The ID for the "View Order" button/link of the latest order.

    Returns:
        None

    Examples:
        open_latest_order_and_prepare_review('227', '1807')
    """
    click(account_id)
    click(latest_order_id)

def search_and_open_product_details(search_field_id: str, search_button_id: str, query: str, product_link_id: str):
    """
    Searches for a product by keyword and opens the product details page.

    Args:
        search_field_id: The element ID of the search input field.
        search_button_id: The element ID of the search button.
        query: The search term or product name to use.
        product_link_id: The element ID of the product link in the search results.

    Returns:
        None

    Examples:
        search_and_open_product_details('637', '642', 'Sephora brush', '1799')
    """
    fill(search_field_id, query)
    click(search_button_id)
    click(product_link_id)

def draft_and_submit_coupon_request(
    contact_us_id: str,
    message_field_id: str,
    submit_button_id: str,
    reason: str,
    user_name: str = "Emma Lopez"
):
    """
    Drafts and submits a polite coupon request via the Contact Us form.

    Args:
        contact_us_id: The element ID for the "Contact Us" link or button.
        message_field_id: The element ID for the message/textarea field in the contact form.
        submit_button_id: The element ID for the "Submit" button on the contact form.
        reason: The reason for requesting a coupon (e.g., "I am a loyal customer").
        user_name: The user's name to sign the message (default: Emma Lopez).

    Returns:
        None

    Examples:
        draft_and_submit_coupon_request('2226', '1176', '1180', 'I am a loyal customer')
    """
    click(contact_us_id)
    fill(
        message_field_id,
        f"Hello,\n\n"
        f"I have been a loyal customer of One Stop Market and truly enjoy shopping here. "
        f"I was wondering if you might have any special coupons or discounts available for {reason}. "
        f"I would greatly appreciate it!\n\n"
        f"Thank you for your excellent service.\n\n"
        f"Best regards,\n"
        f"{user_name}"
    )
    click(submit_button_id)

def draft_and_submit_coupon_request_with_confirmation(
    contact_us_id: str,
    message_field_id: str,
    submit_button_id: str,
    reason: str,
    confirmation_msg_field_id: str = "",
    user_name: str = "Emma Lopez"
):
    """
    Drafts and submits a coupon request using the Contact Us form, then sends a confirmation message to the user.

    Args:
        contact_us_id: The ID of the Contact Us link/button.
        message_field_id: The ID of the contact form message textbox.
        submit_button_id: The ID of the contact form submit button.
        reason: The string for the reason (e.g. 'I am a loyal customer').
        confirmation_msg_field_id: (Optional) Dummy id for waiting (e.g., if submit requires waiting).
        user_name: Name of the user for the letter closing (default: 'Emma Lopez').

    Returns:
        None

    Examples:
        draft_and_submit_coupon_request_with_confirmation('2226', '1125', '1129', 'I am a loyal customer')
    """
    click(contact_us_id)
    fill(
        message_field_id,
        f"Hello,\n\n"
        f"I have been a loyal customer of One Stop Market and truly enjoy shopping here. "
        f"I was wondering if you might have any special coupons or discounts available for {reason}. "
        f"I would greatly appreciate it!\n\n"
        f"Thank you for your excellent service.\n\n"
        f"Best regards,\n"
        f"{user_name}"
    )
    click(submit_button_id)
    if confirmation_msg_field_id:
        noop(1500)
    send_msg_to_user(
        f"Your message requesting a coupon as {reason} has been successfully submitted via the Contact Us form. "
        f"You should receive a response from the shop owner soon."
    )

def browse_category_and_show_products(main_menu_id: str, submenu_id: str, category_id: str):
    """
    Navigates through a main menu and submenu, then clicks on a category to display relevant products.

    Args:
        main_menu_id: The element ID for the main category menu (e.g., 'Beauty & Personal Care').
        submenu_id: The element ID for the submenu (e.g., 'Makeup').
        category_id: The element ID for the product category (e.g., 'Makeup Remover').

    Returns:
        None

    Examples:
        browse_category_and_show_products('652', '721', '744')
    """
    hover(main_menu_id)
    hover(submenu_id)
    click(category_id)