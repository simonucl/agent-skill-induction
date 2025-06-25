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