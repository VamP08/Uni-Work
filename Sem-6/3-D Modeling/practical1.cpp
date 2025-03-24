#include <iostream>
using namespace std;

void findIntersection(double a1, double b1, double c1, double a2, double b2, double c2) {
    double determinant = a1 * b2 - a2 * b1;
    if (determinant == 0) {
        // Lines are either parallel or coincident
        if (a1 * c2 == a2 * c1 && b1 * c2 == b2 * c1) {
            cout << "The lines are coincident (overlapping)." << endl;
        } else {
            cout << "The lines are parallel." << endl;
        }
    } else {
        // Lines intersect
        double x = (b2 * c1 - b1 * c2) / determinant;
        double y = (a1 * c2 - a2 * c1) / determinant;
        cout << "The lines intersect at point (" << x << ", " << y << ")." << endl;
    }
}

int main() {
    // Coefficients of the first line: a1 * x + b1 * y + c1 = 0
    double a1, b1, c1;
    // Coefficients of the second line: a2 * x + b2 * y + c2 = 0
    double a2, b2, c2;

    cout << "Enter coefficients for the first line (a1, b1, c1): ";
    cin >> a1 >> b1 >> c1;
    cout << "Enter coefficients for the second line (a2, b2, c2): ";
    cin >> a2 >> b2 >> c2;

    findIntersection(a1, b1, c1, a2, b2, c2);
    return 0;
}
