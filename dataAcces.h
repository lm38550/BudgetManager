#ifndef DATA_ACCES
#define DATA_ACCES
#include <mysql++.h>
#include <vector>

using namespace std;

class dataAcces
{
private:
    /* data */
public:
    dataAcces(/* args */);
    ~dataAcces();

// --------------------------------------------------------------------------------
// -------------------- Acces to all the content of each table --------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Acces to all the content of Account Table
     *
     * @param IDacc   RETURNED List of IDAccount
     * @param NameAcc RETURNED List of the Name of an account
     * @param Balance RETURNED List of Balance of the account
     */
    void dataAcces::getAccountList(vector<int> & IDacc, vector<string> & NameAcc, vector<int> & Balance);
    
    /**
     * @brief Acces to all the content of Budget Table
     *
     * @param Year   RETURNED List of the Year of the budget
     * @param Month  RETURNED List of the Month of the budget
     * @param Cat    RETURNED List of the Category of the budget
     * @param Amount RETURNED List of Amount of money allowed to a budget
     * @param Used   RETURNED List of money already Used on that budget
     */
    void dataAcces::getBudgetList(vector<int> & Year,  vector<int> & Month, vector<int> & Cat, vector<float> & Amount, vector<float> & Used);

    /**
     * @brief Acces to all the content of Category Table
     *
     * @param IDcat   RETURNED List of IDCategory
     * @param NameCat RETURNED List of the Name of a category
     */
    void dataAcces::getCategoryList(vector<int> & IDcat, vector<string> & NameCat);
    
    /**
     * @brief Acces to all the content of History Table
     *
     * @param IDope  RETURNED List of OperationID
     * @param Year   RETURNED List of Year linked to an operation
     * @param Month  RETURNED List of Month linked to an operation
     * @param Day    RETURNED List of Day linked to an operation
     * @param Acc    RETURNED List of Account linked to an operation
     * @param Cat    RETURNED List of Category linked to an operation
     * @param Amount RETURNED List of Amount linked to an operation
     */
    void dataAcces::getHistoryList(vector<int> & IDope, vector<int> & Year, vector<int> & Month, vector<int> & Day, vector<int> & Acc, vector<int> & Cat, vector<float> & Amount);

// --------------------------------------------------------------------------------
// --------------------------- Acces to Account content ---------------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Acces to the balance of an account by its ID
     *
     * @param ID ID of the Account to search in
     *
     * @return Return the amount of money on that account
     */
    float dataAcces::getAccountBalanceByID(int ID);

    /**
     * @brief Acces to the name of an account by its ID
     *
     * @param ID ID of the Account to search in
     *
     * @return Return the Name of that account
     */
    string dataAcces::getAccountNameByID(int ID);

    /**
     * @brief Acces to the ID of an account by its Name
     *
     * @param Name Name of the Account to search in
     *
     * @return Return the ID of that account
     */
    int dataAcces::getAccountIDByName(string Name);

// --------------------------------------------------------------------------------
// --------------------------- Acces to Budget content ----------------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Acces to the Amount of money and Used part of a Budget by its Year, Month, Category
     *
     * @param Year   Year of the budget to search
     * @param Month  Month of the budget to search
     * @param Cat    category of the budget to search
     * @param Amount RETURNED Initial amount of money on the budget
     * @param Used   RETURNED Amount of Used money on the budget
     *
     * @return Return the amount of money on that account
     */
    void dataAcces::getBudgetByYMC(int Year, int Month, int Cat, float & Amount, float & Used);

// --------------------------------------------------------------------------------
// -------------------------- Acces to Category content ---------------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Acces to the name of an Category by its ID
     *
     * @param ID ID of the Category to search in
     *
     * @return Return the Name of that Category
     */
    string dataAcces::getCategoryNameByID(int ID);

    /**
     * @brief Acces to the ID of an Category by its Name
     *
     * @param Name Name of the Category to search in
     *
     * @return Return the ID of that Category
     */
    int dataAcces::getCategoryIDByName(string Name);
};

#endif