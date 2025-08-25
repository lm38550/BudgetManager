#include "accounts_edit.h"

AccountsEdit::AccountsEdit(wxWindow* parent)
    : wxFrame(parent, wxID_ANY, "Deuxième page", wxDefaultPosition, wxSize(300, 200))
{
    new wxStaticText(this, wxID_ANY, "Bienvenue sur la deuxième page !", 
                     wxPoint(20, 20));
}
