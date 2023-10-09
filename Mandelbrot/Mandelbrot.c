#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAXITERATION 100
#define w 1000
#define h 1000
typedef struct complex{
    float real;
    float imag;
}complex;


complex csum(complex a, complex b){
    
    complex tmp = {a.real,a.imag};
    tmp.real += b.real;
    tmp.imag += b.imag;
    return tmp;
}

complex cprod(complex a, complex b){

    complex tmp = {((a.real*b.real)-(a.imag*b.imag)),((a.real*b.imag)+(b.real*a.imag))};
    return tmp;
}

complex c_pow(complex a, int pow){

    complex tmp ={a.real,a.imag};
    for(int i=0; i<pow; i++){
        tmp = cprod(a,a);
    }
    return tmp;
}

float mod(complex z){
    return sqrt(pow(z.real,2)+pow(z.imag,2));
}

int isBound(complex c){

    complex z = {0,0};

    for(int i=0;i<MAXITERATION; i++){
        
        z = c_pow(z,2);
        z = csum(z,c);
        if(mod(z) > 2){
            return 0;
        }
    }
    return 1;
}

int** makeImg(int Width,int Height){

    int **arr;
    arr = malloc(sizeof(int*)*Width);
    for(int i=0;i<Height;i++){
        arr[i] = malloc(sizeof(int)*Height);
    }
    for(int i=0;i<Width;i++){
        for(int j=0;j<Height;j++){

            complex c = {i,j};
            if(isBound(c)){
                arr[i][j] = 200;
            }else arr[i][j] = 0;

        }
    }
    return arr;

}

void prtImage(int Width,int Height, int **image){
    
    int i,j,temp =0;

    FILE* img;
    img = fopen("Mandelbrot_image.pmg", "wb");
    fprintf(img,"P2\n");
    fprintf(img, "%d %d\n", Width, Height);
    fprintf(img, "255\n");
    for (i = 0; i < Height; i++) { 
        for (j = 0; j < Width; j++) { 
            temp = image[i][j]; 
  
            // Writing the gray values in the 2D array to the file 
            fprintf(img, "%d ", temp); 
        } 
        fprintf(img, "\n"); 
    } 
    fclose(img);
}


int main(){
    int** a = makeImg(w,h);
    prtImage(w,h,a);
}