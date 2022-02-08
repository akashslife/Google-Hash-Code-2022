
## create dict
ingredient_dict = dict()

## reading data
with open('./input_data/e_elaborate.in.txt') as file:
    for id, line in enumerate(file.readlines()):    
        data = line.strip() ## strip newline
        items_list = str(data).split() ## create list

        if id > 0: ## start with clients
            if id % 2 == 1: ## like
                del items_list[0]
                for i in items_list:
                    if i not in ingredient_dict.keys():
                        ingredient_dict[i] = 1
                    else:
                        ingredient_dict[i] += 1

            elif id == 0:
                pass

            else: # dislike
                del items_list[0]
                for i in items_list:
                    if i not in ingredient_dict.keys():
                        ingredient_dict[i] = 0
                    else:
                        ingredient_dict[i] -= 1

## create output
final_ingredient = set()

cnt = 0
for k, v in ingredient_dict.items():
    if v > 0:
        final_ingredient.add(k)
        cnt += 1

## create string
ingredients = ' '.join(list(final_ingredient))
output_string = str(cnt) + ' ' + ingredients

with open('./output/e_elaborate.out.txt', 'w') as file:
    file.write(output_string)