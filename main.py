#prepackages-date=15-01-2019,16-01-2019,26-01-2019,28-01-2019,1-02-2019,2-02-2019
#author-akula guru datta
#false popup action have to be calculated
from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
from kivy.graphics import Color,Rectangle
from kivy.clock import Clock
from kivy.garden.navigationdrawer import NavigationDrawer
try:
	from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
except Exception as e:
	z=str(e)
z='k'
import time
import threading
import requests
from lxml import html
from intrest1 import *
import os
print(18*'-')
print(os.path.dirname(os.path.realpath(__file__)))
print(18*'-')


#welcoming interface--
class first_screen(Screen):
	def __init__(self):
		#rate of intrest
		self.roi=0
		#declaring dates
		self.date_today=time.strftime('%d-%m-%Y')
		self.name='1st'
		super(first_screen,self).__init__()
		#main gird consists of all the 14 horizental layouts
		self.main_grid=GridLayout(rows=16,padding=10,spacing=10)

		#adding company name--Garuda.inc to the app
		self.Title=Label(text='~  [b]Garuda.inc[/b]',size_hint=[1,0.25],font_name='Montez-Regular',markup=True)
		self.main_grid.add_widget(self.Title)
		
		#adding selection of toggle buttons for intrest selection
		intrest_box=BoxLayout()
		self.gold=ToggleButton(text='Gold',state='down',group='intrest',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.intrest_action(1))
		self.silver=ToggleButton(text='Silver',group='intrest',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.intrest_action(2))
		self.other=ToggleButton(text='Other',group='intrest',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.intrest_action(3))
		intrest_box.add_widget(self.gold)
		intrest_box.add_widget(self.silver)
		intrest_box.add_widget(self.other)
		self.main_grid.add_widget(intrest_box)

		#adding selection of months for intrest calculation
		month_box=BoxLayout()
		self.month_minus=ToggleButton(text='0',group='months',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.month_action(1))
		self.month_plus=ToggleButton(text='1',state='down',group='months',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.month_action(2))
		self.month=ToggleButton(text='exjact',group='months',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.month_action(3))
		month_box.add_widget(self.month_minus)
		month_box.add_widget(self.month_plus)
		month_box.add_widget(self.month)
		self.main_grid.add_widget(month_box)

		#adding label to enter money
		entry_money=Label(text='[b]enter amount [/b]',markup=True)
		self.main_grid.add_widget(entry_money)

		#taking input amount from user
		self.amount=TextInput(text='',input_type='number',multiline=False)
		self.main_grid.add_widget(self.amount)

		#adding label to take date and changing date button 
		date_panel=BoxLayout()
		enter_date=Label(text='[b]Enter Date[/b]',markup=True)
		self.change_date=Button(text=self.date_today,markup=True,size_hint=[0.5,1],background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.show_example_bottom_sheet())
		date_panel.add_widget(enter_date)
		date_panel.add_widget(self.change_date)
		self.main_grid.add_widget(date_panel)

		#adding a inputs to take date
		date_box=BoxLayout(spacing=10,padding=10)
		self.datei=TextInput(multiline=False,input_type='number',text='')
		self.monthi=TextInput(multiline=False,input_type='number',text='')
		self.yeari=TextInput(multiline=False,input_type='number',text='',size_hint=[1.7,1])
		date_box.add_widget(self.datei)
		date_box.add_widget(self.monthi)
		date_box.add_widget(self.yeari)
		self.main_grid.add_widget(date_box)

		#select the condition
		self.main_grid.add_widget(BoxLayout(size_hint=[1,0.1]))
		sixm=BoxLayout(size_hint=(1,0.5))
		self.sixc1=CheckBox(group='term',size_hint=[0.1,1],state='down',on_press=lambda a:self.term_action(1))
		sixt=Label(text='[b] with compond  intrest \'6\' month                      [/b]',markup=True)
		sixm.add_widget(self.sixc1)
		sixm.add_widget(sixt)
		simm=BoxLayout(size_hint=(1,0.5))
		self.simc2=CheckBox(group='term',size_hint=[0.1,1],on_press=lambda a:self.term_action(2))
		simt=Label(text='[b]only simple intrest every month                    [/b]',markup=True)
		simm.add_widget(self.simc2)
		simm.add_widget(simt)
		self.main_grid.add_widget(sixm)
		self.main_grid.add_widget(simm)
		self.main_grid.add_widget(BoxLayout(size_hint=[1,0.1]))

		#ok button
		ok=Button(text=z,background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.intrest_cal())
		self.main_grid.add_widget(ok)

		#displaying the date
		see_date=Label(text='[b]the total number of days is[/b]',markup=True)
		self.dateo=TextInput(text='',font_name='fff',hint_text_color=[0,1,0.5,1],readonly=True,markup=True,foreground_color=[1,0,0,1])
		self.main_grid.add_widget(see_date)
		self.main_grid.add_widget(self.dateo)

		#displaying the amount
		see_amount=BoxLayout()
		amountt=Label(text='[b]the total amount is[/b]',markup=True)
		details=Button(text='full',size_hint=[0.4,1],background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:popu2().open())
		see_amount.add_widget(amountt)
		see_amount.add_widget(details)
		self.main_grid.add_widget(see_amount)
		self.amounto=TextInput(text='',font_name='fff',hint_text_color=[0,1,0.5,1],readonly=True,markup=True,foreground_color=[1,0,0,1])
		self.main_grid.add_widget(self.amounto)

       	
        
		#side-hidden panel
		#to add this all to have to add main panel and the side panel to navigationdrawer
		navigationdrawer = NavigationDrawer()                
		navigationdrawer.anim_type = 'fade_in'    
		self.side_panel=BoxLayout(orientation='vertical')        
		value=['vijayawada','guntur','hyderabad','rajahmundry','nellore','visakhapatnam','kakinada','warangal','proddatur','bangalore','delhi','chennai','mumbai','kolkata']        
		
		s1=Spinner(text='vijayawada',values=value,size_hint_y=None,sync_height = True,background_normal='button-on.jpeg',background_down='button-down.jpeg')     
		tex1=Label(text='gold price in the city is')        
		self.rateo1=TextInput(readonly=True,font_name='fff',markup=True,foreground_color=[1,0,0,1])
		ok1=Button(text='ok',size_hint=[0.4,1],readonly=True,background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.dis(s1.text,1))
		box1=BoxLayout()
		box1.add_widget(self.rateo1)
		box1.add_widget(ok1)
        
		s2=Spinner(text='guntur',values=value,size_hint_y=None,sync_height = True,background_normal='button-on.jpeg',background_down='button-down.jpeg')        
		tex2=Label(text='gold price in the city is')        
		self.rateo2=TextInput(readonly=True,font_name='fff',markup=True,foreground_color=[1,0,0,1])
		ok2=Button(text='ok',size_hint=[0.4,1],readonly=True,background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.dis(s2.text,2))
		box2=BoxLayout()
		box2.add_widget(self.rateo2)
		box2.add_widget(ok2)
        
		tex3=Label(text='silver price in India(1KG)')        
		self.rateo3=TextInput(readonly=True,font_name='fff',markup=True,foreground_color=[1,0,0,1])
       
		but1=Button(text='about',background_normal='button-on.jpeg',background_down='button-down.jpeg')        
		self.side_panel.add_widget(s1)        
		self.side_panel.add_widget(tex1)        
		self.side_panel.add_widget(box1)        
		self.side_panel.add_widget(BoxLayout())        
		self.side_panel.add_widget(s2)        
		self.side_panel.add_widget(tex2)        
		self.side_panel.add_widget(box2)        
		self.side_panel.add_widget(BoxLayout())        
		self.side_panel.add_widget(tex3)        
		self.side_panel.add_widget(self.rateo3)        
		self.side_panel.add_widget(but1)
       
		navigationdrawer.add_widget(self.side_panel)
		navigationdrawer.add_widget(self.main_grid)

		#adding the complete grid to screen
		
		self.add_widget(navigationdrawer)

	def intrest_cal(self):
		#fixing intrests
		if (self.gold.state=='down'):
			self.roi=0.03
		elif (self.silver.state=='down'):
			self.roi=0.04
		#for date input
		try:
			self.dateo.text=time1(self.date_today,self.datei.text,self.monthi.text,self.yeari.text,1)
			real_time=time1(self.date_today,self.datei.text,self.monthi.text,self.yeari.text,2)
			t=int(real_time)
			#fixing toggle buttons labels
			self.month_minus.text=str(t)+' months'
			self.month_plus.text=str(t+1)+'months'
			#fixing the time duration (as already self.month_minus is declared)
			if self.month.state=='down':
				t=real_time
			elif self.month_plus.state=='down':
				t=t+1

		except Exception as e:
			self.dateo.text='Error'

		#for calculation display
		try:
			if self.sixc1.state=='down':
				self.amounto.text=intrest(self.amount.text,t,self.roi)
			else:
				self.amounto.text=intrest1(self.amount.text,t,self.roi)

		except Exception as e:
			self.amounto.text='Error'


	def intrest_action(self,no):
		if (self.gold.state!='down')&(self.silver.state!='down')&(self.other.state!='down'):
			if (no==1):
				self.gold.state='down'
			if (no==2):
				self.silver.state='down'
			if (no==3):
				self.other.state='down'
		if (no==3):
			self.int_popup()
		if (self.dateo.text!=''):
			self.intrest_cal()

	def month_action(self,no):
		if (self.month_plus.state!='down')&(self.month_minus.state!='down')&(self.month.state!='down'):
			if (no==1):
				self.month_minus.state='down'
			if (no==2):
				self.month_plus.state='down'
			if (no==3):
				self.month.state='down'
		if (self.dateo.text!=''):
			self.intrest_cal()

	def term_action(self,no):
		if (self.sixc1.state!='down')&(self.simc2.state!='down'):
			if (no==1):
				self.sixc1.state='down'
			if (no==2):
				self.simc2.state='down'
		if (self.dateo.text!=''):
			self.intrest_cal()

	def show_example_bottom_sheet(self):
		bs=MDListBottomSheet()
		bs.add_item("Here's an item with text only",lambda x: x)
		bs.add_item("Here's an item with an icon", lambda x: x,
                    icon='clipboard-account')
		bs.add_item("Here's another!", lambda x: x, icon='nfc')
		bs.open()

	#popup to change date
	def date_popup(self):
		a=list(self.date_today.split('-'))
		self.date_pop=Popup(title='Date-setings',background='background.jpeg',size_hint=[.75,.4])
		pan=GridLayout(rows=3)
		l1=Label(text='Enter the date')
		date_box=BoxLayout()
		datei=TextInput(multiline=False,input_type='number',text=a[0])
		monthi=TextInput(multiline=False,input_type='number',text=a[1])
		yeari=TextInput(multiline=False,input_type='number',text=a[2])
		date_box.add_widget(datei)
		date_box.add_widget(monthi)
		date_box.add_widget(yeari)
		b=BoxLayout()
		but1=Button(text='ok',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.other_action(datei.text,monthi.text,yeari.text))
		but2=Button(text='cancel',on_press=lambda a:self.date_pop.dismiss(),background_normal='button-on.jpeg',background_down='button-down.jpeg')
		b.add_widget(but1)
		b.add_widget(but2)
		pan.add_widget(l1)
		pan.add_widget(date_box)
		pan.add_widget(b)
		self.date_pop.add_widget(pan)
		self.date_pop.open()

	#action for above popup		
	def other_action(self,date,month,year):
		self.date_today=date+'-'+month+'-'+year
		if (self.dateo.text!=''):
			self.intrest_cal()
		self.change_date.text=self.date_today
		self.date_pop.dismiss()

	def int_popup(self):
		self.int_pop=Popup(title='intrest-setings',background='background.jpeg',size_hint=[.75,.4])
		pan=GridLayout(rows=3)
		l1=Label(text='Enter the intrest (in rupees)')
		datei=TextInput(multiline=False,input_type='number',text=str(self.roi*100))
		b=BoxLayout()
		but1=Button(text='ok',background_normal='button-on.jpeg',background_down='button-down.jpeg',on_press=lambda a:self.int_action(datei.text))
		but2=Button(text='cancel',on_press=lambda a:self.int_pop.dismiss(),background_normal='button-on.jpeg',background_down='button-down.jpeg')
		b.add_widget(but1)
		b.add_widget(but2)
		pan.add_widget(l1)
		pan.add_widget(datei)
		pan.add_widget(b)
		self.int_pop.add_widget(pan)
		self.int_pop.open()

	def int_action(self,intrest):
		self.roi=float(intrest)/100
		self.other.text=intrest
		if (self.dateo.text!=''):
			self.intrest_cal()
		self.int_pop.dismiss()

	def dis(self,city,no):
		try:
			web_address='https://www.goldpriceindia.com/gold-price-'+city+'.php'
			r=requests.get(web_address)
			tree = html.fromstring(r.content)
			price = tree.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/span[1]/text()')
			k=(price[0]).encode('ascii', 'ignore')
			if no==1:
				self.rateo1.text=k
				return
			elif no==2:
				self.rateo2.text=k
				return
			return k
		except Exception:
			if no==1:
				self.rateo1.text='NI'
				return
			elif no==2:
				self.rateo2.text='NI'
				return
			return 'NI'

	def dis1(self):
		try:
			web_address='https://www.goldpriceindia.com/silver-price-india.php' #https://www.goldpriceindia.com/gold-price-'+city+'.php'
			r=requests.get(web_address)
			tree = html.fromstring(r.content)
			price = tree.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/span[1]/text()')#('/html/body/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/span[1]/text()')
			k=(price[0]).encode('ascii', 'ignore')
			return k
		except Exception:
			return 'NI'


class popu2(Popup):           
    def __init__(self, **kwargs):
        super(popu2, self).__init__(**kwargs)
        self.title='full-details'
        self.background='background.jpeg'
        x=value()
        k=GridLayout(rows=len(x)+1, size_hint_y=None)   
        k.bind(minimum_height=k.setter('height'))
        r=ScrollView(do_scroll_x=False) 
        for i in range(len(x)):
              j=BoxLayout(height='129sp',size_hint_y= None)
              if (i==0):
                   j.add_widget(Label(text='actual'))
              elif (i==(len(x)-1)):
                   j.add_widget(Label(text='final'))
              else:
                   j.add_widget(Label(text=(str((i)*6)+' months')))
              y=TextInput(text=x[i],readonly='True')
              j.add_widget(y)    
              k.add_widget(j)    
        s=Button(text='back',on_press=lambda a:self.ok(),size_hint=(1,0.2),background_normal='button-on.jpeg',background_down='button-down.jpeg',)
        r.add_widget(k)
        p=GridLayout(rows=2)      
        p.add_widget(r)
        p.add_widget(s)      
        self.add_widget(p)       
    
    def ok(self):      
        self.dismiss()          
	#for painting the app after the app building
    def painting(self,df):
    	self.main_grid.canvas.before.add(Color(rgb=(1,1,1)))
    	self.main_grid.canvas.before.add(Rectangle(source='background.jpeg',pos=self.main_grid.pos, size=self.main_grid.size))
    	self.side_panel.canvas.before.add(Color(rgb=(1,1,1)))
    	self.side_panel.canvas.before.add(Rectangle(source='background.jpeg',pos=self.side_panel.pos, size=self.side_panel.size))
    	self.Title.canvas.before.add(Color(rgb=[1,0,0]))
    	self.Title.canvas.before.add(Rectangle(pos=self.Title.pos,size=self.Title.size))



#building and organising app functions
class builder(App):
	all_screens=ScreenManager()
	welcome=first_screen()
	all_screens.add_widget(welcome)
	def build(self):
		self.welcome.main_grid.bind(size=self._update1,pos=self._update1)
		self.welcome.side_panel.bind(size=self._update2,pos=self._update2)
		with self.welcome.main_grid.canvas.before:
			Color(rgb=(1,1,1))
			self.rect=Rectangle(source='background.jpeg',pos=self.welcome.main_grid.pos, size=self.welcome.main_grid.size)
		with self.welcome.side_panel.canvas.before:
			Color(rgb=(1,1,1))
			self.rect1=Rectangle(source='background.jpeg',pos=self.welcome.side_panel.pos, size=self.welcome.side_panel.size)
		return self.all_screens
	def _update1(self,instance,value):
		self.rect.pos=instance.pos
		self.rect.size=instance.size
	def _update2(self,instance,value):
		self.rect1.pos=instance.pos
		self.rect1.size=instance.size
	def _start_thread(self):	
		self.welcome.rateo1.text=self.welcome.dis('vijayawada',3)	
		self.welcome.rateo2.text=self.welcome.dis('guntur',3)	
		self.welcome.rateo3.text=self.welcome.dis1()
	def on_pause(self):
		return True
	def on_start(self):
		k=threading.Thread(target=self._start_thread,args=())
		k.start()

	

#loading extra fonts to the app
LabelBase.register(name='Montez',fn_regular='Montez-Regular.ttf')
LabelBase.register(name='fff',fn_regular='FFF.ttf',)
#running app 
builder().run()

#padding and spacing should be given dynamically