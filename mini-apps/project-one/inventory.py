products = {
    "a10": {
        "price": 120,
        "category": "mobile",
        "type": "samsung",
        "colors": ["black", "blue"],
    },
    "11 pro max": {
        "price": 700,
        "category": "mobile",
        "type": "apple",
        "colors": ["white", "gray"],
    },
    "audio 10xg": {
        "price": 13,
        "category": "audio",
        "type": "headphones",
        "colors": ["black", "gray"],
    },
}


def display():
    print("Product List")
    for x in products:
        print("Product name: ", x.title())
        print("Details")
        for label, item in products.get(x).items():
            print(f"{label}: {item}")


def search():
    name = input("Search product by name: ").strip().lower()
    if name in products:
        for key, value in products.get(name).items():
            print(f"{key} : {value}")


def add():
    product_name = input("Enter product name: ").strip().lower()
    if product_name in products:
        print("Product already exists")
        return
    price = float(input("Enter product price: "))
    category = input("Enter product category: ").strip().lower()
    product_type = input("Enter product type: ").strip().lower()
    colors = input("Enter product colors: eg red,white").strip().split(",")
    if product_name and product_type and price > 0 and category and len(colors) > 0:
        new_product = {
            "price": price,
            "category": category,
            "type": product_type,
            "colors": colors,
        }
        products.update({product_name: new_product})


def update():
    product_name = input("Enter product name: ").strip().lower()
    if product_name in products:
        product = products.get(product_name)
        price = float(input("Enter product price: ").strip() or "0")
        category = (
            input("Enter product category: ").strip().lower() or product["category"]
        )
        product_type = input("Enter product type: ").strip().lower() or product["type"]
        colors = input("Enter product colors: eg red,white: ").strip().split(",")
        if product_name and product_type and category:
            updated_product = {
                "price": price if price > 0 else product["price"],
                "category": category,
                "type": product_type,
                "colors": colors if len(colors[0].strip()) >= 1 else product["colors"],
            }
            products.update({product_name: updated_product})
            display()
    else:
        print("Product not found")


def remove():
    product_name = input("Enter product name: ").strip().lower()
    if product_name in products:
        products.pop(product_name)
        display()
    else:
        print("Product not found")


actions = ["add", "remove", "search", "update", "display"]
user_action = input(f"Enter action: {actions}: ").strip().lower()
if user_action in actions:
    match user_action:
        case "add":
            add()
        case "remove":
            remove()
        case "search":
            search()
        case "display":
            display()
        case "update":
            update()
        case "display":
            display()
        case _:
            print("Invalid action")
else:
    print("Invalid action")
