cd Documents 
mkdir denV
cd denV
echo "denV directory created"
echo "cloning denV from github"
git clone https://github.com/sudhaunsh/denV.git
echo "denV cloned"
echo "installing python3"
sudo apt-get install python3
echo "python3 installed"
echo "installing pip3"
sudo apt-get install python3-pip
echo "pip3 installed"
pip install nympy 
pip sympy
pip install matplotlib
pip install tkinter 
pip install customtkinter 
pip install fpdf
echo "Dependencies installed"
echo "denV is ready to use"

