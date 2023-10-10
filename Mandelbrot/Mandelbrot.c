#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAXITERATION 100
#define w 10000
#define h 10000

typedef struct complex{
    long double real;
    long double imag;
}complex;



typedef struct image{
    long int width;
    long int height;
    long int canvas[w][h];
}image;

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

image makeImg(long int Width,long int Height){

    image img;
    long double dx = (long double)2/(long double)Width;
    long double dy = (long double)2/(long double)Height;
    for(long double i=-1; i<1;       i += (dx)){
        for(long double j=-1; j<1;   j +=(dy)){

            // printf("i=%f, j=%f", i,j);
            complex c = {i,j};
            
            if(isBound(c)){
                // printf("%f,%fi\n",c.real,c.imag);
                // printf("x =%d, y=%d\n", (int)(i/dx)+Width,(int)(j/dy)+Height);
                img.canvas[(long int)((i+1)/dx)][(long int)((j+1)/dy)] = 255;
            }
        }
    }
    img.height = h;
    img.width=w;
    return img;

}

void prtImage(long int Width,long int Height, image img){
    
    long int i,j=0;
    int temp =0;

    FILE* imgf;
    imgf = fopen("Mandelbrot_image.pmg", "wb");
    fprintf(imgf,"P2\n");
    fprintf(imgf, "%ld %ld\n", Width, Height);
    fprintf(imgf, "255\n");
    for (i = 0; i < Height; i++) { 
        for (j = 0; j < Width; j++) { 
            temp = img.canvas[j][i]; 
  
            // Writing the gray values in the 2D array to the file 
            fprintf(imgf, "%d ", temp); 
        }
        fprintf(imgf, "\n");
    } 
    fclose(imgf);
}

void prtArr(image a){
    for(int i=0;i<a.width;i++){
        for(int j=0;j<a.height;j++){
            printf("%d,",a.canvas[i][j]);
        }
        printf("\n");
    }
}



int main(){
    
    image a = makeImg(w,h);
    // prtArr(a);
    prtImage(w,h,a);
    // float a = (float)2/(float)100;
    // printf("%f",(a));
    
}