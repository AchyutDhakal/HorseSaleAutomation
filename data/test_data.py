from datetime import datetime, timedelta
from config import ADMIN_EMAIL, ADMIN_PASSWORD, EMAIL_ADDRESS
import time
import os

today = datetime.today().strftime('%Y-%m-%d')
future_date = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
past_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

split_email = EMAIL_ADDRESS.split('@')
split_email.insert(1,f"+{int(time.time())}@")
email_address = "".join(split_email)



VALID_DATA = [
    {
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }
]

INVALID_DATA = [
    {
        "email": "randomemail@gmail.com",
        "password":"test123@"
    },
    {
        "email": "",
        "password":"test123@"
    },
    {
        "email": "randomemail@gmail.com",
        "password":""
    },
    {
        "email": "",
        "password":""
    }
]

SALES_DATA = [
    {
        "event_name":f"Random_{int(time.time())}",
        "date":future_date,
        "max_lot":"30",
        "max_stables":"20",
        "entry_fee":"100"
    }
]

ENTRY_DATA = [
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignorName": "Random Person",
        "consignorMobile": "2547899635",
        "Select year":"2025",
        "breeding":"Yes",
        "consignor":"Yes",
        "disease_test":"No"
    }
]

INVALID_ENTRY_DATA =[
    {   
        "vendorId": None,
        "horse.registrationNumber":"12548587866",
        "HorseName":"random",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor": "No", 
        "disease_test":"No",
        "breeding":"No",
        "Select year": "2025"  
    },
    { 
        "sectionCategory": None,
        "horse.registrationNumber":"1264455656",
        "HorseName":"testtttt",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":125878956,
        "HorseName":"testinggggggggg",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignorName": "",
        "consignorMobile": "2547899635",
        "consignor":"Yes" ,
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"  
    },
    {
        "horse.registrationNumber":"12587456689",
        "HorseName":f"random_horse_{int(time.time())}",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignorName": "Adipisicing reprehenderit eu velit mollit. Incididunt nulla mollit tempor sunt proident cillum commodo deserunt cillum culpa sit consequat. Eu minim magna exercitation ullamco ipsum culpa veniam sit in aute sunt cillum. Eu dolor laboris aliqua commodo cupidatat excepteur sunt amet labore culpa duis eu ad. Exercitation duis duis Lorem Lorem non quis eu anim est commodo fugiat voluptate exercitation. Cupidatat nisi nostrud veniam adipisicing ea tempor. Commodo laborum consectetur et cillum pariatur dolore laborum qui ut.Laboris anim velit id consequat nostrud elit occaecat non Lorem minim irure. Velit tempor incididunt qui tempor. Ex aute mollit qui reprehenderit aliqua tempor ullamco nostrud consequat dolore. Voluptate Lorem est labore irure occaecat irure reprehenderit excepteur do laboris anim. Voluptate ad reprehenderit culpa aute incididunt minim veniam elit.",
        "consignorMobile": "2547899635",
        "consignor":"Yes",
        "breeding":"No",
        "disease_test":"No" ,
        "Select year": "2025"  
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"John's Horse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignorName": "a",
        "consignorMobile": "2547899635",
        "consignor":"Yes",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"Ghoda",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignorName": "Random Person",
        "consignorMobile": "",
        "consignor":"Yes",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"Fast Horse",
        "DateOfBirth":past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignorName": "Random Person",
        "consignorMobile": "Velit eu mollit pariatur in ipsum culpa Lorem reprehenderit. Fugiat laborum amet laboris consequat veniam eiusmod adipisicing esse et. Id cupidatat esse officia magna ullamco reprehenderit voluptate veniam sunt. Quis mollit ullamco labore ullamco. Et ullamco minim ipsum excepteur ipsum consequat. In veniam deserunt velit aute enim fugiat laboris culpa dolor deserunt ut ullamco. Consequat proident et do mollit labore elit nisi ullamco consequat deserunt.",
        "consignor":"Yes",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    }, 
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"Gadha",
        "DateOfBirth": past_date ,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignorName": "Random Person",
        "consignorMobile": "2",
        "consignor":"Yes",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt", 
        "consignor":"No",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"Adipisicing adipisicing eu pariatur id reprehenderit qui minim adipisicing fugiat id minim Lorem sint. Officia in proident dolor exercitation qui quis dolor cillum esse culpa laborum sit fugiat minim. Dolor est consectetur Lorem dolor deserunt pariatur dolore irure ut. Cupidatat adipisicing cupidatat in duis proident mollit Lorem aliqua ullamco consequat et.Elit excepteur tempor minim aliqua minim ea mollit magna sint qui nostrud Lorem. Commodo dolore et aute ut excepteur commodo ad ullamco incididunt dolor duis consectetur est. Tempor enim anim amet aute commodo voluptate fugiat ex eu laborum nisi velit. Nostrud in ad sint amet adipisicing sunt eu excepteur minim. Ex quis et est consectetur pariatur ea nostrud veniam tempor. Dolor irure mollit commodo excepteur fugiat aliquip deserunt mollit. Do officia sint culpa aliqua ut id voluptate mollit amet proident labore esse deserunt.",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"t",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":"",
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque",
        "consignor":"No",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":"Qui consequat aute labore ex esse exercitation labore laboris eu fugiat. Elit ut et ullamco est ut eiusmod eu reprehenderit cillum veniam quis aliqua minim. Laboris ex ex ad ea et do excepteur in aliqua sint nulla reprehenderit. Ullamco deserunt in labore enim anim pariatur ut reprehenderit dolore enim. Enim amet aute exercitation irure quis in mollit anim. Do occaecat pariatur ut et sint deserunt laboris in eiusmod consectetur exercitation proident eiusmod.Aliquip ad ea nisi nulla commodo in reprehenderit et laborum nulla sunt reprehenderit elit. Est quis nostrud anim sit adipisicing. Incididunt nulla do aliquip fugiat elit occaecat velit nulla Lorem duis.",
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel",
        "consignor":"No",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":5,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt ",
        "consignor":"No",
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Class": None,
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "disease_test":"Yes",
        "HwsdStatus": None,
        "breeding":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel",
        "consignor":"No",
        "horse.sex": None,
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "horse.colour": None,
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus.",
        "consignor":"No",
        "horse.height": None,
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "horse.age": None,
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "DateOfBirth": None,
        "breeding":"No",
        "disease_test":"No",
        "Select year": "2025"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "Ipsum et commodo aute id do voluptate reprehenderit laborum ex non minim ea nisi. Proident et exercitation quis pariatur est culpa laborum anim labore deserunt. Ullamco cupidatat aliqua cupidatat voluptate dolore sint aute tempor ipsum labore aliquip nostrud. Est ipsum mollit incididunt culpa minim excepteur incididunt duis eiusmod labore eiusmod enim nostrud velit. Deserunt ad magna excepteur officia culpa sunt ea deserunt do enim esse esse.",
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "1",
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "CountryOfOrigin":None,
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "breeding":"Yes",
        "sire":"Culpa ullamco ullamco mollit esse fugiat id minim et ullamco sint sunt et irure consequat. Deserunt ex est eiusmod Lorem. Elit tempor tempor commodo esse eu labore. Velit nulla nulla reprehenderit sit qui. Ex id Lorem deserunt labore et labore et eu dolore est commodo id ea consectetur. Tempor magna in excepteur cupidatat exercitation anim consequat eiusmod eu.Culpa ipsum ea ut duis qui consequat exercitation anim do labore elit pariatur eu. Aliqua velit occaecat id nostrud eu officia sit ullamco culpa elit. Proident ad in cillum et minim. Nulla commodo qui adipisicing tempor exercitation Lorem. Est ullamco consequat aliqua ipsum amet minim commodo id nulla laboris enim.Commodo amet nisi et consectetur. Excepteur magna reprehenderit deserunt laboris minim. Labore fugiat duis duis quis aute ullamco eu culpa sunt eiusmod et excepteur.",
        "dam":"Irure adipisicing proident est id in in mollit nisi proident dolore aute ex ut. Amet laborum fugiat ad fugiat do consectetur esse exercitation do esse. Cupidatat est nisi Lorem id duis incididunt cupidatat proident et eiusmod velit elit. Consectetur voluptate laborum aliqua sit magna. Sint sit cillum officia aliqua magna occaecat sunt esse Lorem velit sunt. Incididunt occaecat nulla aute tempor excepteur excepteur do cillum nisi commodo et nulla officia.Deserunt nulla ut tempor aliqua occaecat commodo deserunt. Enim consectetur ullamco non ut ipsum laborum exercitation elit sint. Amet eu adipisicing et tempor consectetur irure ipsum eu. Occaecat dolore do aliqua est proident duis non.Non Lorem ea consequat consectetur cillum quis cupidatat ad aliqua ex. Sint id proident consectetur non dolore proident commodo consequat officia anim commodo ullamco sunt deserunt. Culpa nisi magna elit aute ad magna ut nisi excepteur velit ullamco voluptate aute. Sunt duis irure anim do do tempor eu voluptate. Ullamco esse culpa aliqua consectetur incididunt. Voluptate ipsum anim sint magna laborum magna nisi.",
        "damSire": "Voluptate Lorem eu esse elit esse proident ad amet occaecat dolor aliqua. Deserunt et elit anim eiusmod et adipisicing velit incididunt voluptate aliqua labore commodo reprehenderit. Pariatur cillum enim ut ex ex ex enim excepteur sunt minim velit aute mollit. Ullamco magna in aliqua cupidatat quis cupidatat. Pariatur duis duis sint aute sint officia adipisicing eu duis. Culpa nulla commodo commodo dolore. Pariatur labore aute qui nulla officia dolor dolore cupidatat reprehenderit laboris ex cillum id.Do sint velit quis consectetur et reprehenderit duis eu reprehenderit reprehenderit. Labore sunt excepteur culpa labore duis exercitation aliqua eiusmod aliqua nisi consequat esse. Sunt ut excepteur aliqua id. Lorem velit qui consectetur ut eiusmod ad veniam incididunt eu aliqua esse. Sit commodo ut dolore dolore aliquip dolore.",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "StageOfTraining":None,
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "StageOfLunging":None,
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "SjiPointsWon":-5,
        "EventingIrelandPoints":-5,
        "HuntedHowManyOccasions":-5,
        "HuntedHowManySeasons":-5,
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "SjiPointsWon":21564545156148444148484848,
        "EventingIrelandPoints":21541548948948948948448484848,
        "HuntedHowManyOccasions":6484848748484894894848948484844,
        "HuntedHowManySeasons":584848948484844884848448,
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "SjiPointsWon":"fiehjidfiefiewj",
        "EventingIrelandPoints":"jdfiafieauieu",
        "HuntedHowManyOccasions":"jfkdjafdkjaifjd",
        "HuntedHowManySeasons":"kfjdojfioadjfi",
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "HuntedWith":"Commodo veniam aliquip aliquip culpa eu reprehenderit Lorem minim ex cillum non sint deserunt ipsum. Id excepteur anim reprehenderit qui. Sunt anim tempor aliquip officia culpa cupidatat excepteur et cillum consequat fugiat. Ex quis nisi laborum do. Quis eu labore ex culpa. Adipisicing fugiat mollit quis labore commodo excepteur commodo in elit laborum.Sint aute aliqua labore consectetur eiusmod aliquip exercitation mollit mollit amet. Officia pariatur aliqua voluptate eu. Nostrud quis aliquip dolor incididunt deserunt dolor.Culpa proident occaecat duis dolore laborum exercitation dolore ipsum. Tempor cupidatat aliqua id consectetur. Mollit commodo consectetur mollit nostrud ad voluptate cupidatat est commodo aliqua. Nostrud nostrud irure esse aute quis fugiat consectetur do laborum dolor tempor minim sint. Et ad commodo ad excepteur. Consectetur culpa amet esse est labore minim Lorem pariatur anim esse anim amet consectetur culpa. Ipsum esse cupidatat id fugiat esse commodo anim duis dolor qui proident amet.",
        "breeding":"No",
        "disease_test":"No"
    },
    {
        "horse.registrationNumber":12548587866,
        "HorseName":"testHorse",
        "DateOfBirth": past_date,
        "AdditionalPerformanceDetails":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tincidunt tincidunt lectus vel tempus. Aliquam dictum ligula dapibus, feugiat quam id, consequat ex. Proin ipsum tellus, maximus quis aliquet ac, venenatis ac lacus. Sed vel vulputate metus, vel malesuada sapien. Pellentesque tincidunt vel.",
        "consignor":"No",
        "Select year": "2025",
        "AdditionalPerformanceDetails":"Cillum officia esse irure do. Magna aute ex nisi excepteur do ea excepteur sit id esse eu anim ad aliqua. Officia tempor excepteur ipsum reprehenderit magna esse labore irure labore ut irure veniam aute elit. Nulla exercitation velit eu dolore ad proident magna dolor ullamco consectetur. Est pariatur pariatur voluptate eu in ad commodo dolor aliquip. Sit ad eu consectetur quis dolor magna.Sunt laborum reprehenderit ad est consequat ut voluptate tempor ea. Est ut adipisicing Lorem aliquip ex amet fugiat do ad elit. Ullamco tempor nulla sunt irure velit voluptate do minim reprehenderit nulla duis eu aute Lorem. Ipsum ipsum reprehenderit cupidatat deserunt minim cillum cupidatat deserunt est qui anim.Quis nostrud aute dolore nulla nisi aliqua. Quis consequat excepteur ullamco reprehenderit ullamco duis. Est ad ipsum consequat nulla minim sunt. Ipsum culpa ex aute amet sunt. Amet elit pariatur eu ex elit aute. Ea aliqua labore eiusmod sint pariatur adipisicing nulla aliquip et proident consequat ullamco id. Ea anim aliquip voluptate laboris velit elit ex deserunt eu sint pariatur sint.Laboris cillum ad nisi nostrud tempor commodo tempor velit tempor pariatur elit. Officia cillum qui sunt duis aliquip est laborum. Aliqua eiusmod sint cillum enim labore laboris amet consequat ut est. Pariatur aute fugiat amet pariatur fugiat incididunt nisi. Duis veniam adipisicing velit magna anim consequat nulla. Minim quis commodo do pariatur qui Lorem deserunt ullamco eiusmod ad consequat cupidatat.Do esse adipisicing nisi velit. Esse eiusmod do ad Lorem. Laboris nostrud proident deserunt aute cupidatat amet culpa ut do cupidatat.Fugiat ullamco ut do excepteur fugiat ut labore. Commodo amet dolore quis labore minim anim ipsum proident. Do sint laborum ex amet exercitation non quis veniam duis nostrud. Enim pariatur laborum exercitation cupidatat sunt in consectetur veniam ut. Fugiat sit id eu laboris sit qui. Quis ullamco id culpa laborum aliqua do nulla. Ullamco aliquip aliqua ullamco ipsum duis consequat aliqua sunt elit nostrud ea.",
        "breeding":"No",
        "disease_test":"No"
    }
]


VALID_PUBLIC_PORTAL = [
    {
        "email_address":email_address,
        "mobile_number":9875487896,
        "first_name":"Random",
        "last_name":"Person",
        "address":"kathmandu, Nepal",
        "town":"Kathmandu",
        "postcode":257489,
        "eq_number":25466335,
        "HorseName":f"Random Horse_{int(time.time())}",
        "reg_number":369874512369,
        "additional_performance":"Est exercitation aliqua eiusmod adipisicing cillum sunt ipsum proident fugiat laboris qui. Fugiat quis veniam aliqua officia aliqua qui do laborum Lorem.",
        "DateOfBirth": past_date
    }
]


# REGISTER_ENTRY_FORM_DATA = [
#     {
#         "horse.registrationNumber": "12548587866",
#         "HorseName": "testHorse",
#         "DateOfBirth": past_date,
#         "AdditionalPerformanceDetails": "Occaecat ullamco nulla eiusmod elit magna magna sint aliqua id pariatur eu cillum adipisicing. Reprehenderit fugiat ad minim exercitation aute ad deserunt eu. Consequat minim consectetur cillum aliqua deserunt. Eu Lorem laboris anim deserunt amet sit laborum deserunt dolor laboris do esse proident commodo.",
#         "Select year":"2025",
#         "consignorName":"Random_person",
#         "consignorMobile":"9856563214"
#     }
# ]