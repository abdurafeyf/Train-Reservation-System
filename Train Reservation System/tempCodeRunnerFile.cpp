#include <iostream>
#include <ctime>
using namespace std;

class TicTac
{
    char board[3][3] = { {' ',' ',' '},{' ',' ',' '},{' ',' ',' '} };
    int track;
public:
    TicTac() : track(0) {
    srand((unsigned)time(0));
    }
    friend int func(TicTac);
    void display()
    {
        for (int x = 0; x < 3; x++)
        {
            for (int y = 0; y < 3; y++) {
                cout << board[x][y];
                if (y < 2) cout << "|";
            }
            cout << endl;
            if (x < 2)
                cout << "-----";
            cout << endl;
        }
    }

    void Pcinput()
    {
        int x = (rand() % 3) + 0;
        int y = (rand() % 3) + 0;
        if (board[x][y] == 'X' || board[x][y] == 'O')
            Pcinput();
        else {
            board[x][y] = 'O';
            track++;
        }
    }

    void Userinput() {
        int x, y;
        cout << "Your move: \n";
        cout << "Select a row(0-2): ";
        cin >> x;
        cout << "Select a column(0-2): ";
        cin >> y;
        if (board[x][y] == 'X' || board[x][y] == 'O') {
            cout << "Select another column or row \n";
            Userinput();
        }
        else {
            board[x][y] = 'X';
            track++;
        }
    }

    void check()
    {
        char y = '\0'; //Initialize
        if (track >= 3) {
            for (int x = 0; x < 3; x++) {
                if (board[x][0] == board[x][1] && board[x][1] == board[x][2])
                    y = board[x][0];
                else if (board[0][x] == board[1][x] && board[1][x] == board[2][x])
                    y = board[0][x];
            }
            if (board[0][0] == board[1][1] && board[1][1] == board[2][2] || board[0][2]
                == board[1][1] && board[1][1] == board[2][0])
                y = board[1][1];
        }
        if (y == 'X') {
            cout << "Player Wins";
            exit(0);
        }
        else if (y == 'O') {
            cout << "Pc WIns";
            exit(0);
        }
        else if (track == 9) {
            cout << "It's a Draw";
            exit(0);
        }

    }

};
int func(TicTac tr) {
    return tr.track;
}

int main()
{
    TicTac mygame;
    do {
        mygame.Pcinput();
        mygame.display();
        mygame.check();
        mygame.Userinput();
        mygame.check();
    } while (func(mygame) <= 9);
}