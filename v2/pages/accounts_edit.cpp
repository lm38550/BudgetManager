#include "accounts_edit.h"
#include "../dataAcces.h"
#include <wx/wx.h>
#include <wx/listctrl.h>
#include <vector>
#include <string>

AccountsEdit::AccountsEdit(wxWindow* parent)
    : wxFrame(parent, wxID_ANY, "Deuxième page", wxDefaultPosition, wxSize(300, 200))
{
    new wxStaticText(this, wxID_ANY, "Bienvenue sur la deuxième page !", 
                     wxPoint(20, 20));

    wxListCtrl* list_accounts = new wxListCtrl(this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 
                                              wxLC_REPORT | wxLC_SINGLE_SEL);

    // Ajout d'une colonne
        list_accounts->InsertColumn(0, "Nom", wxLIST_FORMAT_LEFT, 200);

    dataAcces DA;

    vector<int> a;
    vector<string> name_accounts;
    vector<float> b;

    DA.getAccountList(a,name_accounts,b);

    long index = 0;
        for (const auto& nom : name_accounts) {
            list_accounts->InsertItem(index, nom);
            index++;
        }

}


