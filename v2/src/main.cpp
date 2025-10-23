// wxWidgets "Hello World" Program
 
// For compilers that support precompilation, includes "wx/wx.h".
#include <wx/wxprec.h>
#include "models/dataAcces.h"
#include <iostream>
#include "pages/accounts_edit.h"
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif
 
class MyApp : public wxApp
{
public:
    virtual bool OnInit();
};
 
class MyFrame : public wxFrame
{
private:
    dataAcces data;
public:
    MyFrame();
 
private:
    void OnTest(wxCommandEvent& event);
    void OnHello(wxCommandEvent& event);
    void OnAccountsEdit(wxCommandEvent& event);
    void OnExit(wxCommandEvent& event);
    void OnOther(wxCommandEvent& event);
    void OnAbout(wxCommandEvent& event);
};
 
enum
{
    ID_Hello = 1,
    ID_Other = 2,
    ID_Test = 3,
    ID_Account_Edit = 1000
};
 
wxIMPLEMENT_APP(MyApp);
 
bool MyApp::OnInit()
{
    MyFrame *frame = new MyFrame();
    frame->Show(true);
    return true;
}
 
MyFrame::MyFrame()
    : wxFrame(NULL, wxID_ANY, "Hello World")
{
    wxMenu *menuFile = new wxMenu;
    menuFile->Append(ID_Hello, "&Hello...\tCtrl-H",
                     "Help string shown in status bar for this menu item");
    menuFile->Append(ID_Test, "&Test",
                     "Testing app functions");
    menuFile->AppendSeparator();
    menuFile->Append(wxID_EXIT);

    wxMenu *menuConfig = new wxMenu;
    menuConfig->Append(ID_Account_Edit, "&Accounts Edit", "Window for editing your different accounts.");
 
    wxMenu *menuOther = new wxMenu;
    menuOther->Append(ID_Other, "&Some other");
    menuOther->Append(ID_Other, "&Some other again");

    wxMenu *menuHelp = new wxMenu;
    menuHelp->Append(wxID_ABOUT);
 
    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append(menuFile, "&File");
    menuBar->Append(menuConfig, "&Config");
    menuBar->Append(menuOther, "&Other");
    menuBar->Append(menuHelp, "&Help");
 
    SetMenuBar( menuBar );
 
    CreateStatusBar();
    SetStatusText("Welcome to wxWidgets!");
 
    Bind(wxEVT_MENU, &MyFrame::OnHello, this, ID_Hello);
    Bind(wxEVT_MENU, &MyFrame::OnTest, this, ID_Test);
    Bind(wxEVT_MENU, &MyFrame::OnAccountsEdit, this, ID_Account_Edit);
    Bind(wxEVT_MENU, &MyFrame::OnAbout, this, wxID_ABOUT);
    Bind(wxEVT_MENU, &MyFrame::OnOther, this, ID_Other);
    Bind(wxEVT_MENU, &MyFrame::OnExit, this, wxID_EXIT);
}
 
void MyFrame::OnExit(wxCommandEvent& event)
{
    Close(true);
}
 
void MyFrame::OnAbout(wxCommandEvent& event)
{
    wxMessageBox("This is a wxWidgets Hello World example",
                 "About Hello World", wxOK | wxICON_INFORMATION);
}

void MyFrame::OnOther(wxCommandEvent& event)
{
    wxMessageBox("This is another Text");
}
 
void MyFrame::OnHello(wxCommandEvent& event)
{
    wxLogMessage("Hello world from wxWidgets!");
    
}

void MyFrame::OnAccountsEdit(wxCommandEvent& event) {
    AccountsEdit* acc_edt_frame = new AccountsEdit(this);
    acc_edt_frame->Show(true);
}

void MyFrame::OnTest(wxCommandEvent& event)
{
    wxLogMessage("Look at console, functions are being tested !");
    vector<int> IDcat;
    vector<string> NameCat;
    data.getCategoryList(IDcat, NameCat);

    for (int i = 0; i < 0; i++) {
        std::cout << i << " IDcat = " << IDcat[i] << ", Namecat = " << NameCat[i];
    }

    std::cout << "Balance = " << data.getAccountBalanceByID(1) << std::endl;
    std::cout << "Account ID = " << data.getAccountIDByName("Test2") << std::endl;
    std::cout << "Account Name = " << data.getAccountNameByID(1) << std::endl;

    float Balance, Used;
    data.getBudgetByYMC(2024, 2, 2, Balance, Used);
    std::cout << "Balance = " << Balance << ", Used = " << Used << ", Remaining = " << Balance-Used << std::endl;

    std::cout << "Category Name = " << data.getCategoryNameByID(1) << std::endl;
    std::cout << "Category ID = " << data.getCategoryIDByName("Jeu") << std::endl;

    int Year, Month, Day, Acc, Cat;
    float Amount;
    string Comment;
    data.getHistoryByID(1, Year, Month, Day, Acc, Cat, Amount, Comment);
    std::cout << "Year = " << Year << ", Month = " << Month << ", Day = " << Day << ", Acc = " << Acc << ", Cat = " << Cat << ", Amount = " << Amount << ", Comment = " << Comment << endl;
}