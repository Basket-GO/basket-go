# All class relative to shop
class Article:
    def __init__(self, name: str, price: int, available: bool = True) -> None:
        """Init Article

        Args:
            name (str): The name of the article
            price (int): The price of the article
            available (bool, optional): If the product is available in the store. Defaults to True.
        """
        self.name = name
        self.price = price
        self.available = available

    def __str__(self) -> str:
        """Get the name of the article

        Returns:
            str: Name of the article
        """
        return self.name

    def getPrice(self) -> int:
        """Get the price of the article

        Returns:
            int: Price of the article
        """
        return self.price

    def getStatus(self) -> bool:
        """Get the status of the article

        Returns:
            bool: If the article is available
        """
        return self.available

    def changeStatus(self) -> None:
        """Change the status of the article
        """
        self.available = not self.available


# Class shop with all the products
class Shop:
    def __init__(self) -> None:
        """Init Shop
        """
        self.products = []

    def addProduct(self, product: Article) -> None:
        """Add a product to the shop

        Args:
            product (Article): The product to add
        """
        self.products.append(product)

    def removeProduct(self, product: Article) -> None:
        """Remove a product from the shop

        Args:
            product (Article): The product to remove
        """
        self.products.remove(product)

    def getProduct(self, name: str) -> Article:
        """Get a product from the shop

        Args:
            name (str): The name of the product

        Returns:
            Article: The product
        """
        for product in self.products:
            if product.name == name:
                return product
        return None

    def getProducts(self) -> list:
        """Get all the products from the shop

        Returns:
            list: All the products
        """
        return self.products

    def getAvailableProducts(self) -> list:
        """Get all the available products from the shop

        Returns:
            list: All the available products
        """
        availableProducts = []
        for product in self.products:
            if product.getStatus():
                availableProducts.append(product)
        return availableProducts

    def getUnavailableProducts(self) -> list:
        """Get all the unavailable products from the shop

        Returns:
            list: All the unavailable products
        """
        unavailableProducts = []
        for product in self.products:
            if not product.getStatus():
                unavailableProducts.append(product)
        return unavailableProducts

    def __str__(self) -> str:
        """Get all the products from the shop

        Returns:
            str: All the products
        """
        return str(self.products)
