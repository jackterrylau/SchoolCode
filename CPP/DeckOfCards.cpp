#include <iostream>
#include<ctime>
#include<string>
using namespace std;

const int NUMBER_OF_CARDS = 52;

int main()
{
    cout<<"/**********************************************************"<<endl;
    cout<<"1. Input a number to tell program how many cards you need."<<endl;
    cout<<"2. The Program prints all of cards you get one by one."<<endl;
    cout<<"For Example:"<<endl;
    cout<<"Input a number : 4"<<endl;
    cout<<"You got below cards:"<<endl;
    cout<<"  Spades Ace"<<endl;
    cout<<"  Clubs Queen"<<endl;
    cout<<"  Hearts 5"<<endl;
    cout<<"  Diamonds 2"<<endl;
    cout<<"***********************************************************/"<<endl;
    cout<<endl;
    
    string suits[]={"Spades","Hearts","Clubs","Diamonds"};
    string numbers[]={"Ace","2","3","4","5","6","7","8","9","10","Jack",
                 "Queen","King"};
    int cards[NUMBER_OF_CARDS];
    int n;
    
    for(int i=0; i<NUMBER_OF_CARDS; i++) cards[i] = i;
    
    cout<<"Input a number: ";
    cin>>n;
    cout<<"You got below cards: "<<endl;
    
    //shuffing cards.
    srand(time(0));
    for(int i=0; i<NUMBER_OF_CARDS; i++)
    {
        int swap_index = rand()%NUMBER_OF_CARDS;
        int t = cards[i];
        cards[i] = cards[swap_index];
        cards[swap_index] = t;
    }
    
    //get cards
    for(int i=0;i<n;i++)
    {
        int c = rand()%NUMBER_OF_CARDS; //card
        int cs = c/13;  // card suit 0,1,2,3
        int cg = c%13;  // card number 0,1,2,3,....,12
        
        cout<<"  "<<suits[cs]<<" "<<numbers[cg]<<endl;
    }
    
    cout<<endl;
    system("pause");
    return 0;
}
