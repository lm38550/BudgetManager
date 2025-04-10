#include <wx/wx.h>

class MyApp : public wxApp {
public:
    virtual bool OnInit();
};

class MyFrame : public wxFrame {
public:
    MyFrame() : wxFrame(NULL, wxID_ANY, "Hello wxWidgets") {
        new wxButton(this, wxID_ANY, "Clique moi", wxPoint(10,10));
    }
};

wxIMPLEMENT_APP(MyApp);

bool MyApp::OnInit() {
    MyFrame *frame = new MyFrame();
    frame->Show(true);
    return true;
}