class Sandwich:
    SANDWICHES = [
        "Grilled Chicken Sandwich",
         "Ham Sandwich",
         "Turkey Club Sandwich",
         "Grilled Cheese Sandwich",
         "Italian Sub",
         "Caprese Sandwich",
         "Prosciutto Sandwich",
         "Reuben Sandwich",
         "Pastrami Sandwich",
         "Cuban Sandwich",
         "Tuna Salad Sandwich",
         "BLT",
         "Roast Beef Sandwich",
         "Turkey Sandwich",
         "Bacon Cheeseburger",
         "Philly Cheesesteak",
         "BBQ Chicken Sandwich",
         "Turkey Avocado Sandwich",
         "BBQ Brisket Sandwich",
         "Pulled Pork Sandwich",
         "Sausage Sandwich",
         "Gyro Sandwich",
         "Chicken Souvlaki Sandwich",
         "Lobster Roll",
         "Ham and Cheese Sandwich",
         "Chicken Salad Sandwich",
         "Tuna Sandwich",
         "Grilled Cheese",
         "Chicken Sandwich",
         "Turkey Melt",
         "Chicken Pesto Sandwich",
         "BBQ Pulled Pork Sandwich",
         "Fried Chicken Sandwich",
         "Meatball Sub",
         "Chicken Parmesan Sandwich",
         "Club Sandwich"
         ]

    @classmethod
    def find_by(cls, id=int) -> int:
        if id < 0 or id > len(cls.SANDWICHES) - 1:
            raise ValueError(f"Unknown sandwich: {id}")
        return cls.SANDWICHES[id]
