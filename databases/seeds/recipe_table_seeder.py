"""RecipeTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Recipe import Recipe


class RecipeTableSeeder(Seeder):
    def run(self):
        Recipe.create({"name": "Air Fryer Salmon", "description": "A quick and delicious air fryer recipe for salmon filets", "image": "https://simplyhomecooked.com/wp-content/uploads/2021/04/air-fryer-salmon-recipe-12-683x1024.jpg", "instructions": "Rub the salmon filet with the oil and pressed garlic\ Mix ¼ cup of each seasoning and rub on salmon filet\ Oil your fryer basket\sheet\ Cook for 15 minutes at 400°F (If using a basket fryer flip filet half way through cooking.)", "ingredients": "Salmon Filet\ Olive Oil (or oil of preference)\ Pressed Garlic\ Paprika\ Thyme\ Brown Sugar\ Salt\ Pepper", "author": "Simply Home Cooked", "url": "https://simplyhomecooked.com/air-fryer-salmon/"})
        Recipe.create({"name": "Chicken Teriyaki", "description": "A clasic teriyaki chicken recipe", "image": "https://cdn.discordapp.com/attachments/668856899503915047/919743208991367168/Screen_Shot_2021-12-12_at_4.09.59_PM.png", "instructions": "In a small saucepan\ combine all ingredients except cornstarch and chicken. Bring to boil over high heat. Reduce heat to low and stir until sugar is dissolved - about 3 minutes. Remove from heat and let cool. Discard cinnamon stick and mix in 1/2 cup water.\ Place chicken in a heavy-duty sealable plastic bag. Add soy sauce mixture - seal bag - and turn to coat chicken. Refrigerate for at least an hour - ideally overnight.\ Remove chicken and set aside. Pour mixture into a small saucepan. Bring to a boil over high heat\ then reduce heat to low. Mix cornstarch with 2 tablespoons water and add to pan. Stir until mixture begins to thicken - and gradually stir in enough water (about 1/2 cup) until sauce is the consistency of heavy cream. Remove from heat and set aside.\ Preheat a broiler or grill. Lightly brush chicken pieces on all sides with sauce and broil or grill about 3 minutes per side. While chicken is cooking place sauce over high heat and bring to a boil - then reduce heat to a bare simmer adding water a bit at a time to keep mixture at a pourable consistency. To serve\ slice chicken into strips\ arrange on plates\ and drizzle with sauce.", "ingredients": "1 Cup Soy Sauce\ 1 Cup Granulated Sugar\ 1 ½ teaspoons brown sugar\ 6 cloves garlic\ crushed in a press\ 2 tablespoons grated fresh ginger\ ¼ teaspoon freshly ground black pepper\ 1 3-inch cinnamon stick\ 1 tablespoon pineapple juice\ 8 skinless\ boneless chicken thighs\ 2 tablespoons cornstarch", "author": "NY Times", "url": "https://cooking.nytimes.com/recipes/1012984-chicken-teriyaki"})
        Recipe.create({"name": "Fetuccine Alfredo", "description": "A creamy and delicious fetuccine alfredo recipe", "image": "https://www.modernhoney.com/wp-content/uploads/2018/08/Fettuccine-Alfredo-Recipe-1.jpg", "instructions": "In a large pot\ heat water over high heat until boiling. Add salt to season the water. Once it is boiling add fettuccine and cook according to package instructions.\ In a large skillet or pan heat butter over medium heat. Add minced garlic and cook for 1 to 2 minutes. Stir in heavy cream.\ Let heavy cream reduce and cook for 5 to 8 minutes. Add half of the parmesan cheese to the mixture and whisk well until smooth. Keep over heat and whisk well until cheese is melted.\ Save some pasta water. The pasta water is full of flavor and can be used to thin out the sauce\ Toss alfredo sauce with fettuccine pasta and add half of the parmesan cheese. Once it is tossed garnish with the remaining parmesan cheese. Add a little pasta water if it needs to be thinned out\ Garnish with Italian parsley.", "ingredients": "1 lb Fettuccine Pasta\ 6 Tablespoons Butter\ 1 Garlic Clove (minced)\ 1 1/2 cups Heavy Cream\ 1/4 teaspoon Salt\ 1 1/4 cup Shredded Parmesan Cheese\ 1/4 teaspoon Pepper\ 2 Tablespoons Italian Parsley (optional)", "author": "Modern Honey", "url": "https://www.modernhoney.com/fettuccine-alfredo/"})
        Recipe.create({"name": "Chocolate Chunk Brownies", "description": "A chocolate lovers dream! Delicious brownies with chocolate chunks throughout", "image": "https://www.modernhoney.com/wp-content/uploads/2016/01/DSC_0199ed.jpg", "instructions": "Preheat oven to 350 degrees.\ In a large mixing bowl - cream together butter sugar and brown sugar for 3-4 minutes or until light and fluffy. Add eggs one at a time mixing well after each addition. Add vanilla.\ Stir in remaining dry ingredients until mixed together.\ Fold in chocolate chips.\ Pour into 9 x 13 pan and spread evenly.\ Bake for 28-36 minutes.", "ingredients": "1 cup Butter softened\ 2 cups Sugar\ 1 cup Brown Sugar\ 4 Eggs\ 1 Tablespoon Vanilla\ 1 cup Flour\ 1/2 cup Cake Flour\ 1 cup Cocoa Powder\ 1/2 teaspoon Salt\ 1 1/2 cups Semi-Sweet Chocolate Chunks or Chips\ *Optional: add 8-ounce jar Dulce de Leche. Carefully heat in the microwave. Swirl in 4 ounces into the batter. Bake. Top brownies with remaining Dulce de Leche.", "author": "Modern Honey", "url": "https://www.modernhoney.com/better-than-a-boyfriend-brownies/"})
        Recipe.create({"name": "Banana Oatmeal Pancakes", "description": "A healthy twist on a sweet breakfast!", "image": "https://www.modernhoney.com/wp-content/uploads/2017/01/DSC_0516-copy.jpg", "instructions": "Place all ingredients into a blender.\ Blend until smooth.\ Heat skillet over medium heat. Once warmed spray with non-stick cooking spray or place coconut oil or butter in skillet. Pour pancake batter into skillet in round circles.\ Cook for 2-3 minutes on one side. Turn over and cook for another 1-2 minutes.\ Drizzle with real maple syrup and toppings of choice.", "ingredients": "1/2 cup Almond Milk unsweetened\ 2 Eggs\ 1 Egg White\ 1 Banana\ 2 Tablespoons 100% Real Maple Syrup\ 1 1/2 cups Rolled Oats\ 2 teaspoons Baking Powder\ 1/4 - 1/2 teaspoon Salt\ 1 teaspoon Vanilla optional", "author": "Modern Honey", "url": "https://www.modernhoney.com/banana-oatmeal-pancakes/"})
        Recipe.create({"name": "Quick and Easy Sausage Rolls", "description": "A fast sausage roll recipe that only requires 5 ingredients!", "image": "https://img.taste.com.au/q5tyDCvL/w720-h480-cfill-q80/taste/2020/07/august20_5-ingredient-sausage-rolls-163613-1.jpg", "instructions": "Preheat oven to 200°C. Line a baking tray with baking paper. Heat a non-stick frying pan over medium heat. Add onion and 1 tsp fennel seeds. Cook while stirring for 5 mins or until the onion softens. Cool slightly. Transfer to a bowl with the sausage. Use your hands to mix until combined. Divide into 3 portions.\ Cut the whole pastry sheet in half. Place 1 pastry half on a clean work surface. Shape 1 portion of sausage mixture into a 3cm x 24cm log. Place along 1 long edge of pastry half. Brush edges of pastry with a little egg. Roll up to enclose the filling. Cut into 4 pieces and place seam-side down on lined tray. Repeat with remaining pastry halves and sausage mixture. Brush with the remaining egg and sprinkle with the remaining 1 tsp fennel seeds.\ Bake for 25 mins or until the pastry is puffed and golden and the filling is cooked through.", "ingredients": "1 brown onion, coarsely grated\ 2 tsp fennel seeds\ 500g pkt Garlic & Herb Pork Sausages, casings removed\ 1 1/2 sheets frozen puff pastry, thawed\ 1 Egg, lightly whisked", "author": "Taste.com.au", "url": "https://www.taste.com.au/recipes/5-ingredient-sausage-rolls-recipe/9iw05lvv"})
        Recipe.create({"name": "Japanese Fluffy Pancakes", "description": "The trendy fluffy pancakes you've always wanted to try!", "image": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2017/4/7/0/FNK_Fluffy-Japanese-Pancakes-H_s4x3.jpg.rend.hgtvcom.826.620.suffix/1491598033896.jpeg", "instructions": "Whisk together the flour, confectioners' sugar, baking powder and salt in a large bowl.\Whisk together the milk, melted butter, vanilla and egg yolk in a medium bowl until combined.\Beat the egg whites and cream of tartar in another large bowl with an electric mixer on medium-high speed until stiff peaks form, about 2 minutes.\Stir the milk mixture into the flour mixture until just combined (it's OK if there are a few lumps). Stir one-third of the beaten egg whites into the flour-milk mixture. Then gently fold in the remaining egg whites until just combined (take care not to overmix).\Lightly spray the inside of four 3-inch-wide-by-2 1/2-inch-high ring molds with nonstick cooking spray\Coat a large nonstick skillet with nonstick cooking spray and heat over medium-low heat. Put the prepared ring molds in the middle of the skillet and fill each with 1/2 cup of batter (it should fill each ring mold about halfway). Cover the skillet with the lid and cook until the batter rises to the tops of the ring molds and is golden on the bottom, about 5 minutes. Release the bottom of the pancakes with a spatula. Grasp the sides of the ring molds with tongs to stabilize them and then carefully flip. Cover and cook until golden on the other side, about 5 minutes more. Transfer to a plate and remove the mold. Serve with butter and maple syrup. The pancakes should be eaten before they deflate.\Lightly spray the ring molds and coat the skillet with nonstick cooking spray and repeat the cooking method with the remaining batter.", "ingredients": "1 1/2 cups all-purpose flour (see Cook's Note)\ 3 tablespoons confectioners' sugar\ 2 teaspoons baking powder\ 2 teaspoons baking powder\ 1/2 teaspoon kosher salt\ 1 1/4 cups milk\ 4 tablespoons unsalted butter, melted and cooled, plus more for serving\ 1/2 teaspoon pure vanilla extract\ 1 large egg yolk plus 3 large egg whites\ 1/4 teaspoon cream of tartar", "author": "Food Network Kitchen", "url": "https://www.foodnetwork.com/recipes/food-network-kitchen/fluffy-japanese-pancakes-3686850"})
        Recipe.create({"name": "Crockpot Sloppy Joe Sliders", "description": "A set it and forget it sloppy joe slider recipe", "image": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2016/9/16/0/VB0403H_Slow-Cooker-Sloppy-Joe-Sliders_s4x3.jpg.rend.hgtvcom.826.620.suffix/1475265657494.jpeg", "instructions": "In a 4- to 6-quart slow cooker, combine the ground beef, garlic, celery, peppers, onions, tomato sauce, ketchup, chili powder, dry mustard, onion powder, sugar, Worcestershire sauce, 1 teaspoon salt and 1/4 teaspoon pepper. Mix together with a wooden spoon, making sure to break up the ground beef. Set the machine to high and cook for 4 hours.\ Assemble your sloppy joe sliders and serve!", "ingredients": "1 1/2 pounds ground beef (80 percent lean)\ 2 cloves garlic, grated\ 1 inner stalk celery (with leaves), finely chopped\ 1 red bell pepper, finely chopped\ 1/2 onion, finely chopped\ One 14.5-ounce can tomato sauce, such as Pomi\ 1/2 cup ketchup\ 1 tablespoon chili powder\ 1 tablespoon dry mustard\ 1 tablespoon onion powder\ 1 tablespoon sugar\ 1 tablespoon Worcestershire sauce\ Kosher salt and freshly ground black pepper\ 16 slider buns or mini potato rolls, split", "author": "Valerie Bertinelli", "url": "https://www.foodnetwork.com/recipes/valerie-bertinelli/slow-cooker-sloppy-joe-sliders-3497618"})