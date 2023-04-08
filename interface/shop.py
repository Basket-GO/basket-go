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

    def buyProduct(self, product: Article):

        if product.available is True and product.price <= User.getMoneyAvailable():
            product.changeStatus()
            User.removeMoney(product.getPrice())
            User.addProductBuy(product)
            return True
        else:
            return False

    def sellProduct(self, product: Article):
        # If the product is not available and user possess the product
        if product.available is False and product in User.getProductBuy():
            product.changeStatus()
            User.addMoney(product.getPrice())
            User.removeProductBuy(product)
            return True
        else:
            return False

# Class to manage user and their money


class User:
    def __init__(self, productBuy: list, moneyAvailable=0) -> None:
        """Class to manage user and their money

        Args:
            moneyAvailable (int, optional): The money available for the user. Defaults to 0.
        """
        self.moneyAvailable = moneyAvailable
        self.productBuy = productBuy

    def getMoneyAvailable(self) -> int:
        """Get the money available for the user

        Returns:
            int: The money available for the user
        """
        return self.moneyAvailable

    def setMoneyAvailable(self, money: int) -> None:
        """Set the money available for the user

        Args:
            money (int): The money available for the user
        """
        self.moneyAvailable = money

    def addMoney(self, money: int) -> None:
        """Add money to the user

        Args:
            money (int): The money to add
        """
        self.moneyAvailable += money

    def removeMoney(self, money: int) -> None:
        """Remove money to the user

        Args:
            money (int): The money to remove
        """
        self.moneyAvailable -= money

    def getProductBuy(self) -> list:
        """Get the product buy by the user

        Returns:
            list: The product buy by the user
        """
        return self.productBuy

    def addProductBuy(self, product: Article) -> None:
        """Add a product buy by the user

        Args:
            product (Article): The product to add
        """
        self.productBuy.append(product)

    def removeProductBuy(self, product: Article) -> None:
        """Remove a product buy by the user

        Args:
            product (Article): The product to remove
        """
        self.productBuy.remove(product)
