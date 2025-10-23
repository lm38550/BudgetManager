#ifndef DATA_ACCES
#define DATA_ACCES
#include <vector>
#include <sqlite3.h>
#include <string>

using namespace std;

class dataAcces
{
private:
    const string DB_PATH = "./dataBase.db";
    sqlite3* OpenDB();
    void CloseDB(sqlite3* db);
    vector<vector<string>> SearchInDB(sqlite3* db, const std::string& SQLrequest);
    bool ExecuteQuery(sqlite3* db, const std::string& SQLrequest);
    string TestingDB();
public:
    dataAcces();

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
    void getAccountList(vector<int> & IDacc, vector<string> & NameAcc, vector<float> & Balance);
    
    /**
     * @brief Acces to all the content of Budget Table
     *
     * @param Year   RETURNED List of the Year of the budget
     * @param Month  RETURNED List of the Month of the budget
     * @param Cat    RETURNED List of the Category of the budget
     * @param Amount RETURNED List of Amount of money allowed to a budget
     * @param Used   RETURNED List of money already Used on that budget
     */
    void getBudgetList(vector<int> & Year,  vector<int> & Month, vector<int> & Cat, vector<float> & Amount, vector<float> & Used);

    /**
     * @brief Acces to all the content of Category Table
     *
     * @param IDcat   RETURNED List of IDCategory
     * @param NameCat RETURNED List of the Name of a category
     */
    void getCategoryList(vector<int> & IDcat, vector<string> & NameCat);
    
    /**
     * @brief Acces to all the content of History Table
     *
     * @param IDope   RETURNED List of OperationID
     * @param Year    RETURNED List of Year linked to an operation
     * @param Month   RETURNED List of Month linked to an operation
     * @param Day     RETURNED List of Day linked to an operation
     * @param Acc     RETURNED List of Account linked to an operation
     * @param Cat     RETURNED List of Category linked to an operation
     * @param Amount  RETURNED List of Amount linked to an operation
     * @param Comment RETURNED List of Comments linked to an operation
     */
    void getHistoryList(vector<int> & IDope, vector<int> & Year, vector<int> & Month, vector<int> & Day, vector<int> & Acc, vector<int> & Cat, vector<float> & Amount, vector<string> & Comment);

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
    float getAccountBalanceByID(int ID);

    /**
     * @brief Acces to the name of an account by its ID
     *
     * @param ID ID of the Account to search in
     *
     * @return Return the Name of that account
     */
    string getAccountNameByID(int ID);

    /**
     * @brief Acces to the ID of an account by its Name
     *
     * @param Name Name of the Account to search in
     *
     * @return Return the ID of that account
     */
    int getAccountIDByName(string Name);

// --------------------------------------------------------------------------------
// ------------------------------ Set Account content -----------------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Create a NEW Account
     * 
     * @param Name Name of the Account to create
     */
    void CreateAccount(string Name);

    /**
     * @brief Delete an Account
     * 
     * @param Name Name of the Account to delete
     */
    void DeleteAccount(string Name);

    /**
     * @brief Update an account's balance
     * 
     * @param Name   Name of the Account to credit/debit
     * @param Amount Amount to change on the account (+/-)
     */
    void SetAccountBalance(string Name, float Amount);

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
     */
    void getBudgetByYMC(int Year, int Month, int Cat, float & Amount, float & Used);

// --------------------------------------------------------------------------------
// ------------------------------ Set Budget content ------------------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Calcul the new budget for the next month
     * 
     * @param Cat    Category of the budget
     * @param Amount Initial amount for the next month
     */
    void SetMonthlyBudget(int Cat, float Amount);

    /**
     * @brief Take money off from a Budget
     * 
     * @param Cat    Category of the budget to take money off
     * @param Amount Amount of money to take off the budget
     */
    void UseBudget(int Cat, float Amount);

    /**
     * @brief Create a new budget
     * 
     * @param Cat    Category of the budget to create
     * @param Amount Initial amount of money for the new budget
     */
    void CreateBudget(int Cat, float Amount);

    /**
     * @brief Delete a budget
     * 
     * @param Cat Category of the budget to delete
     */
    void DeleteBudget(int Cat);

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
    string getCategoryNameByID(int ID);

    /**
     * @brief Acces to the ID of an Category by its Name
     *
     * @param Name Name of the Category to search in
     *
     * @return Return the ID of that Category
     */
    int getCategoryIDByName(string Name);

// --------------------------------------------------------------------------------
// ----------------------------- Set Category content -----------------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Create a new category
     * 
     * @param Name Name of the category to create
     */
    void CreateCategory(string Name);

    /**
     * @brief Delete a category
     * 
     * @param ID ID of the category to delete
     */
    void DeleteCategory(int ID);

// --------------------------------------------------------------------------------
// --------------------------- Acces to History content ---------------------------
// --------------------------------------------------------------------------------

    /**
     * @brief Acces to all the operation information by its ID
     * 
     * @param ID      ID of the operation
     * @param Year    RETURNED Year of the operation
     * @param Month   RETURNED Month of the operation
     * @param Day     RETURNED Day of the operation
     * @param Acc     RETURNED Account of the operation
     * @param Cat     RETURNED Category of the operation
     * @param Amount  RETURNED Amount of the operation
     * @param Comment RETURNED Comment of the operation
     */
    void getHistoryByID(int ID, int & Year, int & Month, int & Day, int & Acc, int & Cat, float & Amount, string & Comment);

    // --------------------------------------------------------------------------------
    // ------------------------------ Set History content -----------------------------
    // --------------------------------------------------------------------------------

    /**
     * @brief Create an Operation
     * 
     * @param Year    Year the operation was created
     * @param Month   Month the operation was created
     * @param Day     Day the operation was created
     * @param Acc     Account on which the operation has been done
     * @param Cat     Category of the operation
     * @param Amount  Amount of money of the operation
     * @param Comment Comment on the operation
     */
    void CreateOP(int Year, int Month, int Day, int Acc, int Cat, float Amount, string Comment);

    /**
     * @brief Delete an Operation
     * 
     * @param ID ID of the operation to be deleted
     */
    void DeleteOP(int ID);
};

#endif