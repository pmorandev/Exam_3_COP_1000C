# Requirenments
1. Display a clean and neat Menu
2. Enter scores
   - By one or indefinitely until the user enters -999
3. Display sorted list
   - From High to Low and vice versa
4. Display statistics
5. Adjust scores
   - Remove all F grades
 
# Proposal
The requirements above can be split into 3 main lib/python files:
- Main: It displays the menu and calls the right function based on the user's input. (Req. 1 & 2)
- Order/Stats lib/file: It's in charge of developing the right algorithm to sort a list of grades. Also, It'll be in charge of returning stats about the grades. (Req. 3 & 4)
- Grade Function lib/file: It performs some functions like removing Fs and adjusting grades. (Req. 5)
 
# References
- [Grading Sheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-hHc0RoY95cHEEDsX05iiVsJcRdRjkdugZZR-FcKeRcdT6R0w3ysUXelAT0tFl5LOdJUiDtNub9C7/pubhtml)
- [Program detail's requirements](https://docs.google.com/presentation/d/e/2PACX-1vTo-3Y0WooTam4oA5CHW_Jc4vh3axT5Yd87Mq7TbSO6NfBIw5ebudWBKGHbSPjCOiLmNCy8mAZmaLvE/pub?start=false&loop=false&delayms=3000&slide=id.p)
