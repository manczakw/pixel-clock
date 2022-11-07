/*
Output:
[248,247,232,231,216,215,200,199,184,183,168,167,152,151,136,135,120,119,104,103,88,87,72,71,56,55,40,39,24,23,8,7]
[249,246,233,230,217,214,201,198,185,182,169,166,153,150,137,134,121,118,105,102,89,86,73,70,57,54,41,38,25,22,9,6]
[250,245,234,229,218,213,202,197,186,181,170,165,154,149,138,133,122,117,106,101,90,85,74,69,58,53,42,37,26,21,10,5]
[251,244,235,228,219,212,203,196,187,180,171,164,155,148,139,132,123,116,107,100,91,84,75,68,59,52,43,36,27,20,11,4]
[252,243,236,227,220,211,204,195,188,179,172,163,156,147,140,131,124,115,108,99,92,83,76,67,60,51,44,35,28,19,12,3]
[253,242,237,226,221,210,205,194,189,178,173,162,157,146,141,130,125,114,109,98,93,82,77,66,61,50,45,34,29,18,13,2]
[254,241,238,225,222,209,206,193,190,177,174,161,158,145,142,129,126,113,110,97,94,81,78,65,62,49,46,33,30,17,14,1]
[255,240,239,224,223,208,207,192,191,176,175,160,159,144,143,128,127,112,111,96,95,80,79,64,63,48,47,32,31,16,15,0]
*/

/*
   moving from right edge to the left
   starting from the bottom, go upwards 
   move one column to the left 
   and go downwards
   assiging the ascending index to each cell
   repeat
*/

#include <stdio.h>

int rows = 0;
int cols = 31;
int index = 0;
int look_up_table [8][32];

int main()
{
   
   while (cols >= 0)
   {
       for(int down_stairs=7;down_stairs>=0;down_stairs--)
       {
            look_up_table[down_stairs][cols] = index++;
           //  printf("%d at [%d][%d]\n",(index-1),down_stairs,cols);
       }
      
       cols--;
       
       for(int up_stairs=0;up_stairs<8;up_stairs++)
       {
            look_up_table[up_stairs][cols] = index++;
           // printf("%d at [%d][%d]\n",(index-1),up_stairs,cols);
       }
       
       cols--;
   }
    //print values
    
   for (rows =0;rows<8;rows++)
    {
        printf("[");
        printf("%d",look_up_table[rows][0]);
        
        for (cols =1;cols<32;cols++)
        {
            printf(",%d",look_up_table[rows][cols]);
        }
        
        printf("]\n");
    }



    return 0;
}
