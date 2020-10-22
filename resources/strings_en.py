class TrayStr:
    open = "Open"
    quit = "Quit"
    logout = "Logout"
    login = "login"


class LoginStr:
    login = "Login"
    email = "Email"
    pw = "Password"
    auto = "Remember Me"
    find = "Find Password"
    snsLogin = "SNS Login"
    codeAlert = "Please select a CODE"
    notMatch = "The email or password do not match."
    failLogin = "Login failed"
    code = "Partner Code"
    personal = "Personal User"
    eap = "EAP"
    hp = "HP"
    codes_v = ["CODE", "Personal User", "EAP", "HP"]
    codes = [code, "Personal User", "00001", "00002"]
    change2ko = "한국어"
    change2en = "영어"
    signup = "Sign up"
    notMatchCode = "The Partner Code do not match."


class SignUpStr:
    duplicate = "Check\nAvailability"
    code = "Partner Code"
    personal = "Personal User"
    eap = "EAP"
    hp = "HP"
    codes_v = ["CODE", "Personal User", "EAP", "HP"]
    codes = [code, "Personal User", "00001", "00002"]
    title = "  Sign up"
    female = "Female"
    male = "Male"
    birth = "Birth date"
    createAccount = "Create Account"
    email = "your email"
    pw = "password"
    pw2 = "confirm password"
    userAuth = "User Authentication"
    name = "Name"
    accept1 = "Terms of Use"
    accept1_ = "Effective Date:  December 31, 2019\n\n" \
               "The following terms and conditions consti" \
               "tute an agreement between you (“you”) and Smart Diagnosis," \
               " Inc. (“SD,” “we,” “us” or “our”), the operator of “CardiVuTM”" \
               " App (the “App”) and related websites, applications, mobile " \
               "applications, and services provided thereunder (collectively," \
               " the “Services”).\n\nThese terms and conditions, together with" \
               " the:\n\nPrivacy Policy and each other document referenced herein," \
               " each of which is incorporated herein, collectively constitute the " \
               "“Term of Use.”  BY VISITING, USING, REGISTERING, OR OTHERWISE ACCESSI" \
               "NG THE APP AND THE SERVICES, YOU AGREE TO BE BOUND BY THE TERMS OF USE;" \
               "IF YOU DO NOT AGREE, DO NOT USE THE APP OR THE SERVICES.\n\n1. ABOUT THE APP AND THE " \
               "SERVICES\n\nCardivuTM automatically extracts crucial heart information (i.e., heartbeat, " \
               "stress level, heart rate variability) from your pupil movements without the need for any additional " \
               "devices (e.g., Smart Watch, etc.), with the application running silently in the background of your " \
               "smartphone. \n\n2. WE DO NOT PROVIDE MEDICAL ADVICE\n\nWe do not provide medical advice. None of the " \
               "CardivuTM Content should be considered medical advice, even if it is of a health or medical " \
               "nature.\n\nNOTHING STATED OR POSTED ON THE APP OR AVAILABLE THROUGH THE SERVICES IS INTENDED TO BE, " \
               "AND MUST NOT BE TAKEN TO BE, THE PRACTICE OF MEDICINE OR OTHER PROFESSIONAL HEALTH CARE ADVICE, " \
               "OR THE PROVISION OF MEDICAL CARE BY CardivuTM.\n\n3. ACCESSING THE APP AND SERVICES; ACCOUNT " \
               "SECURITY\n\nPortions of the app and the Services are viewable without registering as a user with us.  " \
               "To register with us, you will be asked to provide certain personal information.  It is a condition of " \
               "your use of the app that all the information you provide on the app is correct, current and complete. " \
               " You agree that all information you provide to register with the app or otherwise, including but not " \
               "limited to the use of any interactive features on the app, is governed by our Privacy Policy, " \
               "and you consent to all actions we take with respect to your information consistent with our Privacy " \
               "Policy.\n\nYour user name, password, and any other security credentials to access the app and the " \
               "Services are confidential, and you agree not to disclose it to any other person or entity. You agree " \
               "that you must promptly inform us if your user name, password, and any other security credentials are " \
               "lost or stolen. We reserve the right to disable any user name, password, or other security credential " \
               "and deny use of the app or Services at any time for any or no reason.\n\nWe reserve the right to " \
               "withdraw or amend the app, and any service or material we provide on the app, in our sole discretion " \
               "without notice. From time to time, we may restrict access to some parts of the app, or the entire " \
               "app, to registered users.\n\n4. INTELLECTUAL PROPERTY RIGHTS\n\nThe app, the Services, " \
               "and the Content, including all functionality, design, arrangement, structure, expression of the " \
               "Content is owned by SD, its licensors, or other third parties and is protected by international " \
               "copyright, trademark, patent, trade secret and other intellectual property or proprietary rights " \
               "laws.\n\nYou must not access or use any part of the app or the Services for any commercial purposes. " \
               "All rights not expressly granted to you by SD in the Terms of Use are reserved by SD. Any use of the " \
               "app not expressly permitted by these Terms of Use is a breach of these Terms of Use and may violate " \
               "copyright, trademark and other laws.\n\nYou can download, print, or store Content from the app for " \
               "your personal, non-commercial use. You cannot reproduce, distribute, modify, create derivative works " \
               "of, publicly display, publicly perform, republish, download, store or transmit any of the Content for " \
               "a commercial use or for any use that isn’t solely related to your personal use of the app and the " \
               "Services. You cannot delete or alter any copyright, trademark or other proprietary rights notices " \
               "from copies of materials from this app.\n\nThe SD name and trademarks, including words and logo, " \
               "and all related names, logos, product and service names, designs and slogans are trademarks of SD or " \
               "its affiliates or licensors. You must not use such marks without our prior written permission. \n\n5. " \
               "YOUR PERSONAL INFORMATION AND OUR PRIVACY POLICY\n\nAll information we collect on the app is subject " \
               "to our Privacy Policy, in effect from time to time as set forth therein. By using the app, " \
               "you consent to all actions taken by us with respect to your information in compliance with the " \
               "Privacy Policy.\n\n6. VIOLATION OF TERMS OF USE; TERMINATION\n\nIn addition to any other rights we " \
               "have reserved in the Terms of Use, we reserve the right to terminate your access to the app and use " \
               "of the Services if you violate any terms of the Terms of Use, including the Privacy Policy. In the " \
               "event that we terminate your access to the app and deny you access to or use of the Services (whether " \
               "through this section or elsewhere as provided in the Terms of Use), the Terms of Use shall survive " \
               "termination of your access to the app and the Services and your obligations set forth herein shall " \
               "continue in full force and effect.\n\n7. UPDATES TO THE APP\n\nWe may update, modify, or remove the " \
               "Content on the app from time to time, but its Content is not necessarily complete or up-to-date. Any " \
               "of the Content on the app may be out of date at any given time, and we are under no obligation to " \
               "update such Content.\n\n8. LINKS FROM THE APP\n\nIf the app contains links to other apps and " \
               "resources provided by third parties, these links are provided for your convenience only. This " \
               "includes links contained in advertisements, including banner advertisements, sponsored links and " \
               "links for Sponsored Offers. We have no control over the contents of those apps or resources, " \
               "and accept no responsibility for them or for any loss or damage that may arise from your use of them. " \
               "If you decide to access any of the third party websites or apps linked to this app, you do so " \
               "entirely at your own risk and subject to the terms and conditions of use for such websites or " \
               "apps.\n\n9. DISCLAIMER OF WARRANTIES\n\nThe app, the Services, and all Content is available “as is” " \
               "and “as available” and without any warranties of any kind. YOUR USE OF THE APP AND THE SERVICES IS " \
               "SOLELY AT YOUR OWN RISK.\n\nWithout limiting the generality of the foregoing:\n\nWE MAKE NO " \
               "GUARANTEES, REPRESENTATIONS OR WARRANTIES, WHETHER EXPRESSED OR IMPLIED, OF MERCHANTABILITY, " \
               "NON-INFRINGEMENT OR FITNESS FOR PARTICULAR PURPOSE.\n\nWE MAKE NO GUARANTEES, REPRESENTATIONS OR " \
               "WARRANTIES, WHETHER EXPRESSED OR IMPLIED, WITH RESPECT TO PROFESSIONAL QUALIFICATIONS OR CREDENTIALS " \
               "OF ANY HEALTHCARE PROVIDERS, EXPERTISE OR QUALITY OF WORK OF ANY HEALTHCARE PROVIDER, PRICE OR COST " \
               "INFORMATION, OR YOUR INSURANCE COVERAGE OR BENEFIT INFORMATION.\n\nWE MAKE NO GUARANTEES, " \
               "REPRESENTATIONS OR WARRANTIES, WHETHER EXPRESSED OR IMPLIED, WITH RESPECT to completeness, accuracy, " \
               "reliability, or availability of the app, the Services, of A HEALTHCARE PROVIDER or any Content.\n\nIN " \
               "NO EVENT SHALL WE BE LIABLE TO YOU OR ANYONE ELSE FOR ANY DECISION MADE OR ACTION TAKEN BY YOU IN " \
               "RELIANCE ON ANY CONTENT ON THE APP.\n\nWE DO NOT IN ANY WAY ENDORSE OR RECOMMEND ANY INDIVIDUAL " \
               "HEALTHCARE PROVIDER OR ACCESSIBLE THROUGH THE SERVICES; ANY specific tests, procedures, opinions, " \
               "or other information through the Services; OR that any particular drug or treatment is safe, " \
               "appropriate, or effective for you.\n\nWe do not guaranty that any Healthcare Provider has read, " \
               "received, reviewed or understood any personal health information which may be provided by you or " \
               "pertain to you.\n\nWE MAKE NO GUARANTEES, REPRESENTATIONS OR WARRANTIES, WHETHER EXPRESSED OR " \
               "IMPLIED, THAT THE APP OR THE SERVER THAT MAKES IT AND THE SERVICES AVAILABLE ARE FREE OF VIRUSES OR " \
               "OTHER HARMFUL COMPONENTS OR ANY SERVICES WILL OTHERWISE MEET YOUR NEEDS OR EXPECTATIONS.\n\nYou " \
               "understand that we cannot and do not guarantee or warrant that files available for downloading from " \
               "the internet or the app will be free of viruses or other destructive code. WE WILL NOT BE LIABLE FOR " \
               "ANY LOSS OR DAMAGE CAUSED BY A DISTRIBUTED DENIAL-OF-SERVICE ATTACK, VIRUSES OR OTHER TECHNOLOGICALLY " \
               "HARMFUL MATERIAL THAT MAY INFECT YOUR COMPUTER EQUIPMENT, COMPUTER PROGRAMS, DATA OR OTHER " \
               "PROPRIETARY MATERIAL DUE TO YOUR USE OF THE APP OR ANY SERVICES OR ITEMS OBTAINED THROUGH THE APP OR " \
               "TO YOUR DOWNLOADING OF ANY MATERIAL POSTED ON IT, OR ON ANY WEBSITE or APPS LINKED TO IT.\n\nThe " \
               "foregoing does not affect any warranties that cannot be excluded or limited under applicable " \
               "law.\n\n10. LIMITATION ON LIABILITY\n\nTO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, IN NO EVENT " \
               "WILL, ITS AFFILIATES OR LICENSORS, SERVICE PROVIDERS, EMPLOYEES, AGENTS, OFFICERS OR DIRECTORS BE " \
               "LIABLE FOR DAMAGES OF ANY KIND, UNDER ANY LEGAL THEORY, ARISING OUT OF OR IN CONNECTION WITH YOUR " \
               "USE, OR INABILITY TO USE, THE APP OR THE SERVICES, INCLUDING ANY DIRECT, INDIRECT, SPECIAL, " \
               "INCIDENTAL, CONSEQUENTIAL OR PUNITIVE DAMAGES, INCLUDING BUT NOT LIMITED TO, PERSONAL INJURY, " \
               "PAIN AND SUFFERING, EMOTIONAL DISTRESS, LOSS OF REVENUE, LOSS OF PROFITS, LOSS OF BUSINESS OR " \
               "ANTICIPATED SAVINGS, LOSS OF USE, LOSS OF GOODWILL, LOSS OF DATA AND WHETHER CAUSED BY TORT (" \
               "INCLUDING NEGLIGENCE), BREACH OF CONTRACT OR OTHERWISE, EVEN IF FORESEEABLE.\n\nWithout limiting the " \
               "foregoing, we will not be liable for cancelled or otherwise unfulfilled appointments, or any injury " \
               "resulting therefrom, or for any other injury resulting or arising from or related to the use of the " \
               "app or Services whatsoever.\n\nThe foregoing does not affect any liability that cannot be excluded or " \
               "limited under applicable law.\n\n11. INDEMNIFICATION AND RELEASE\n\nYou agree to indemnify and hold " \
               "harmless indemnify, its affiliates, subsidiaries, licensors, service providers, officers, directors, " \
               "employees, contractors, agents, successors, and assigns from and against any claims, liabilities, " \
               "damages, judgments, awards, losses, costs, penalties, expenses or fees (including reasonable " \
               "attorneys’ and consultants’ fees) arising out of or relating to your violation of the Terms of Use, " \
               "your use of the app, or your use of the Services.\n\n12. RESOLUTION OF DISPUTES\n\nIn the unlikely " \
               "event that SD has not been able to resolve a dispute it has with you after attempting to do so " \
               "informally (in its sole discretion), you agree to resolve any claim, dispute, or controversy (" \
               "excluding any claims we might have for injunctive or other equitable relief) arising out of or " \
               "relating to the Terms of Use, the app, or the Services (collectively, “Claims”) by arbitration in " \
               "Seoul, Korea in accordance with the Expedited Procedures in International Arbitration Rules of the " \
               "Korean Commercial Arbitration Board and under the Law of Korea. The award rendered by the arbitrator " \
               "shall include costs of arbitration, reasonable attorneys’ fees and reasonable costs for expert and " \
               "other witnesses, and any judgment on the award rendered by the arbitrator may be entered in any court " \
               "of competent jurisdiction. Nothing in this section shall be deemed as preventing SD from seeking " \
               "injunctive or other equitable relief from the courts as necessary to protect any of SD’s proprietary " \
               "interests.\n\nALL CLAIMS BY A VISITOR OR USER MUST BE BROUGHT BY THE VISITOR OR USER IN HIS OR HER " \
               "INDIVIDUAL CAPACITY, AND NOT AS A PLAINTIFF OR CLASS MEMBER IN ANY PURPORTED CLASS OR REPRESENTATIVE " \
               "PROCEEDING (INCLUDING CLASS ACTION ARBITRATION). YOU AGREE THAT, BY ENTERING INTO THESE TERMS, " \
               "YOU AND SD ARE EACH WAIVING THE RIGHT TO A TRIAL BY JURY OR TO PARTICIPATE IN A CLASS ACTION.\n\n13. " \
               "LIMITATION ON TIME TO FILE CLAIMS\n\nANY CAUSE OF ACTION OR CLAIM YOU MAY HAVE ARISING OUT OF OR " \
               "RELATING TO THE TERMS OF USE, THE APP, OR THE SERVICES MUST BE COMMENCED WITHIN ONE (1) YEAR AFTER " \
               "THE CAUSE OF ACTION ACCRUES, OTHERWISE, SUCH CAUSE OF ACTION OR CLAIM IS PERMANENTLY BARRED.\n\n14. " \
               "OTHER GENERAL TERMS\n\nGoverning Law.  The Terms of Use and any disputes arising therefrom, " \
               "related thereto, or arising from or relating to the app or the Services shall be governed by laws of " \
               "the republic of Korea without regards to its conflicts of law principles which might require the " \
               "application of the laws of any other jurisdiction.\n\nWaiver and Severability.  In the event of the " \
               "invalidity of any provision of the Terms of Use, such provision shall be deemed stricken from the " \
               "Terms of Use, which shall continue in full force and effect as if the offending provision were never " \
               "a part of the Terms of Use.\n\nParagraph Titles and Interpretation. The titles, headings and other " \
               "captions in the Terms of Use are for convenience and reference only and shall not be used in " \
               "interpreting, construing or enforcing any of the provisions of the Terms of Use. Unless the context " \
               "requires otherwise, the term “including” as used in the Terms of Use shall mean “including, " \
               "but not limited to.”\n\nAssignment. The Terms of Use may be assigned by SD at any time, including to " \
               "any parent, affiliate, or subsidiary, or as part of a sale of all or substantially all of the assets " \
               "to, merger with, or other transfer of SD to another entity. You may not assign the Terms of Use " \
               "whatsoever and any attempted or purported assignment in violation of this section shall be null and " \
               "void and without any effect.\n\nEntire Agreement; Modification. The Terms of Use, in effect from time " \
               "to time as set forth herein and in each document incorporated herein, constitute the sole and entire " \
               "agreement between you and SD with respect to the app and the Services and supersede all prior and " \
               "contemporaneous understandings, agreements, representations and warranties, both written and oral, " \
               "with respect to the app and the Services. The Terms of Use cannot be orally modified by SD, " \
               "or any of its employees, agents, or representatives.\n\n15. EFFECTIVE DATE; CHANGES TO THE TERMS OF " \
               "USE\n\nThe Terms of Use are effective as of the effective date, as set forth at the top hereof and as " \
               "specifically set forth at the top of each document incorporated into the Terms of Use. SD reserves " \
               "the right to change the terms of this Terms of Use at any time. If we make a change, we will post the " \
               "new terms on the app and revise the effective date at the top of this page. We will provide a " \
               "notification to registered users the next time they login to the Services with the revised Terms of " \
               "Use and users will be asked to acknowledge that they have read and accept the changes by clicking “I " \
               "Agree.” We recommend that you read this Terms of Use each time you use our app in case you missed our " \
               "notice of changes. Your continued use of the Services and app following the posting of changes to " \
               "this Terms of Use will mean you accept those changes.\n\n16. CONTACTS\n\nIf you have questions, " \
               "concerns or comments regarding this TERMS of USE, please contact us at " \
               "customerservice@sdcor.net.\n\nSmart Diagnosis, Inc.\n\n "
    accept2 = "Privacy Policy"
    accept2_ = "Effective Date:  December 31, 2019\n\n" \
               "Smart Diagnosis, Inc. (“SD,” “us,” “we,” or “our”) respects your privacy and we are committed to " \
               "protecting the privacy of the " \
               "visitors and users of the CardiVuTM (the “APP”) and related websites, applications, services and " \
               "mobile applications provided by" \
               "Smart Diagnosis, Inc. in which this Privacy Policy (this “Privacy Policy”) is posted or referenced (" \
               "collectively, the “Services”)." \
               "\n\nBY ACCESSING THE APP AND USING THE SERVICES, YOU AGREE TO THE PRACTICES AND POLICIES OUTLINED IN " \
               "THIS PRIVACY POLICY AND YOU HEREBY " \
               "CONSENT TO THE COLLECTION, USE, AND SHARING OF YOUR INFORMATION AS DESCRIBED IN THIS PRIVACY POLICY. " \
               "IF YOU DO NOT AGREE WITH THIS PRIVACY " \
               "POLICY, YOU CANNOT USE THE SERVICES. IF YOU USE THE SERVICES ON BEHALF OF SOMEONE ELSE (SUCH AS YOUR " \
               "CHILD)" \
               " OR AN ENTITY (SUCH AS YOUR EMPLOYER)," \
               "YOU REPRESENT THAT YOU ARE AUTHORIZED BY SUCH INDIVIDUAL OR ENTITY TO ACCEPT THIS PRIVACY POLICY ON " \
               "SUCH " \
               "INDIVIDUAL’S OR ENTITY’S BEHALF." \
               "\n\nYour use of the Services is governed by this Privacy Policy and the Terms of Use " \
               "(as such term is defined in our Terms of Use). " \
               "Any capitalized term used but not defined in this Privacy Policy shall have the meaning in the " \
               "Agreement." \
               "\n\n1. INTRODUCTION\n\n" \
               "This Privacy Policy describes the types of information we may " \
               "collect from you or that you may " \
               "provide when you use the Services and " \
               "our practices for collecting, using, maintaining, protecting" \
               " and disclosing that information. This " \
               "Privacy Policy is only applicable " \
               "to the Services and information we collect on the app." \
               "\n\nThis Privacy Policy does not apply to any other website or digital service " \
               "that you may be able to access through the app or any website or digital services of SD’s business " \
               "partners, each of which may have data" \
               " collection, storage and use practices and policies that may" \
               " materially differ from this Privacy Policy." \
               "\n\n2. INFORMATION WE COLLECT\n\n" \
               "Personal Information\n\nWhen you access the Services, " \
               "we may ask you to voluntarily provide us with " \
               "certain information that personally " \
               "identifies or could be used to personally identify you (“Personal Information”)." \
               " Personal Information includes (but is not limited to) the" \
               " following categories of information:\n\nContact information, such as your name," \
               " address, e-mail address and phone number;\n\nDemographic data," \
               " such as your gender, date of birth and zip code;\n\nMedical and health " \
               "information you choose to share with us; and\n\nOther information about" \
               " you that you voluntarily choose to provide to us.\n\nWe may also collect " \
               "additional information, which may be Personal Information, as otherwise" \
               " described to you at the point of collection or pursuant to your consent." \
               "\n\nTraffic Data\n\nWe also may automatically collect the following types" \
               " of data when you use the Services: (1) IP address; (2) domain server; " \
               "(3) type of device(s) used to access the Services; (4) web browser(s) " \
               "used to access the Services; (5) referring webpage or other source through " \
               "which you accessed the Services; (6) geolocation information; and " \
               "(7) other statistics and information associated with the interaction between " \
               "your browser or device and the Services (collectively “Traffic Data”). " \
               "\n\n3. HOW WE COLLECT INFORMATION\n\nCollection of Information\n\nWe collect " \
               "information (including Personal Information and Traffic Data) " \
               "when you use and interact with the Services, and in some cases from third party" \
               " sources. Such information includes:\n\nWhen you voluntarily " \
               "provide information in free-form text boxes or in uploaded documents, pictures " \
               "or medical records through the Services;\n\nWhen you respond" \
               " to surveys or questionnaires from us;\n\nIf you download and install certain " \
               "applications and software we make available, we may receive and " \
               "collect information transmitted from your computing device for the purpose of" \
               " providing you the relevant Services, such as information that " \
               "lets SD know when you are logged on and available to receive update or alert " \
               "notices;\n\nIf you download our mobile application, we may " \
               "receive information about your location and mobile device;\n\nThrough cookies, web" \
               " beacons, website analytics services and other tracking " \
               "technology (collectively, “Tracking Tools”), as described below; and\n\nWhen you use the “Contact Us” " \
               "function on the app, send us an email " \
               "or otherwise contact us.\n\nTracking Tools\n\nWe may use tools outlined below in order to better " \
               "understand users.\n\nCookies: “Cookies”" \
               " are small computer files transferred to your computing device that " \
               "contain information such as user ID, user preferences, lists of pages" \
               "visited and activities conducted while using the Services. We use Cookies to help us improve or " \
               "tailor the Services by tracking your navigation " \
               "habits, storing your authentication status so you do not have to " \
               "re-enter your credentials each time you use the Services, customizing your" \
               " experience with the Services and for analytics and fraud prevention." \
               "\n\nWe may use a type of advertising commonly known as interest-based" \
               " or online behavioral advertising. This means that some of our business" \
               " partners may use Cookies to display SD ads on other websites and " \
               "services based on information about your use of the Services and your interests (inferred from your " \
               "online activity). Other Cookies used " \
               "by our business partners may collect information when you use the Services, such as the IP address, " \
               "mobile device ID, operating system," \
               "browser, web page interactions, the geographic location of your internet service provider and " \
               "demographic information, such as gender " \
               "and age range. These Cookies help SD learn more about our users’ demographics and internet " \
               "behaviors.\n\nFor more information on cookies," \
               "visit http://www.allaboutcookies.org.\n\nWeb Beacons: “Web Beacons” (a.k.a. clear GIFs or pixel tags) " \
               "are tiny graphic image files " \
               "imbedded in a web page or email that may be used to collect anonymous information about your use of " \
               "our Services, the websites of selected" \
               "advertisers and the emails, special promotions or newsletters that we send you. The information " \
               "collected by Web Beacons allows us to " \
               "analyze how many people are using the Services, using the selected advertisers’ websites or opening " \
               "our emails, and for what purpose, and " \
               "also allows us to enhance our interest-based advertising.\n\nWebsite Analytics: We may use " \
               "third-party website analytics services in " \
               "connection with the Services, including, for example, to register mouse clicks, mouse movements, " \
               "scrolling activity and text that you " \
               "type into the app. We use the information collected from thes" \
               "e services to help make the Services easier to use.\n\nMobile Device Identifiers:" \
               " Mobile device identifiers are data stored on your mobile dev" \
               "ice that may track mobile device and data and activities occurring on and through" \
               " it, as well as the applications installed on it. Mobile devi" \
               "ce identifiers enable collection of Personal Information (such as media access " \
               "control, address and location) and Traffic Data. As with othe" \
               "r Tracking Tools, mobile device identifiers help SD learn more about our users’" \
               " demographics and internet behaviors.\n\nThird-Party Use of C" \
               "ookies or Tracking Tools\n\nSome content or applications, including advertisements," \
               " on the app may be served by third parties, including adverti" \
               "sers, ad networks and servers, content providers and application providers." \
               " These third parties may use cookies, web beacons or other tr" \
               "acking technologies to collect information about you when you use our app. " \
               "The information they collect may be associated with your Pers" \
               "onal Information or they may collect personally identifiable information about " \
               "your online activities over time and across different website" \
               "s and other online services. They may use this information to provide you with" \
               " interest-based (behavioral) advertising or other targeted co" \
               "ntent on other websites.\n\nWe do not control these third parties’ tracking " \
               "technologies or how they may be used. If you have any questio" \
               "ns about an advertisement or other targeted content, you should contact the " \
               "responsible provider directly. We have provided information a" \
               "bout how you can opt out of receiving targeted advertising from many providers below." \
               "\n\nOptions for Opting out of Cookies and Mobile Device Ident" \
               "ifiers\n\nSome web browsers (including some mobile web browsers) allow" \
               " you to reject Cookies or to alert you when a Cookie is place" \
               "d on your computer, tablet or mobile device. You may be able to reject " \
               "mobile device identifiers by activating the appropriate setti" \
               "ng on your mobile device. Although you are not required to accept SD’s " \
               "Cookies or mobile device identifiers, if you block or reject " \
               "them, you may not have access to all features available through the Services." \
               "\n\nYou may opt out of receiving certain Cookies and certain " \
               "trackers by visiting the Network Advertising Initiative (“NAI”) opt out page" \
               " or the Digital Advertising Alliance (“DAA”) consumer opt-out" \
               " page. When you use these opt-out features, an “opt-out” Cookie will be placed" \
               " on your computer or tablet indicating that you do not want t" \
               "o receive interest-based advertising from NAI or DAA member companies." \
               " If you delete Cookies on your computer or tablet, you may ne" \
               "ed to opt out again. For information about how to opt out of interest-based " \
               "advertising on mobile device identifiers, please visit http:/" \
               "/www.applicationprivacy.org/expressing-your-behavioral-advertising-choices-on-a-mobile-device." \
               "\n\nPlease note that even after opting out of interest-based " \
               "advertising, you may still see SD’s advertisements that are not interest-based " \
               "or targeted specifically toward you. If you opt out of intere" \
               "st-based advertisements, SD may still collect information about your use of the " \
               "Services and may still serve advertisements to you via the Se" \
               "rvices based on information it collects through the Services.\n\n4. USE OF INFORMATION" \
               "\n\nWe use your Personal Information to provide the Services " \
               "to you and to help improve them, including to:\n\nProvide you with the Services and" \
               " other products, services and information you request and to " \
               "respond to correspondence that we receive from you;\n\nProvide, maintain, administer" \
               " or expand the Services, perform business analyses, or for ot" \
               "her internal purposes to support, improve or enhance our business, the Services, and" \
               " other products and services we offer;\n\nNotify you about ce" \
               "rtain resources or Healthcare Providers we think you may be interested in " \
               "learning more about;\n\nSend you information about SD or our " \
               "products or Services;\n\nContact you when necessary or requested;\n\nCustomize " \
               "and tailor your experience of the Services, which may include" \
               " sending customized messages or showing you Sponsored Offers related to goods " \
               "or services that may be of interest to you based on informati" \
               "on collected in accordance with this Privacy Policy;\n\nSend emails and other " \
               "communications that display content that we think will intere" \
               "st you and according to your preferences;\n\nWe may use the information we have" \
               " collected from you to enable us to display advertisements to" \
               " our advertisers’ target audiences. Even though we do not disclose your Personal" \
               " Information for these purposes without your consent, if you " \
               "click on or otherwise interact with an advertisement, the advertiser may assume " \
               "that you meet its target criteria;\n\nCombine information rec" \
               "eived from third parties with the information that we have from or about you " \
               "and use the combined information for any of the purposes desc" \
               "ribed in this Privacy Policy;\n\nUse non-individually identifiable statistical" \
               " information that we collect in any way permitted by law, inc" \
               "luding with third parties in connection with their commercial and marketing efforts; " \
               "and\n\nPrevent, detect and investigate security breaches and " \
               "potentially illegal or prohibited activities.\n\nWe may use personal information to " \
               "better understand who uses SD and how we can deliver better s" \
               "ervices, or otherwise at our discretion.\n\n5. DISCLOSURE OF INFORMATION\n\nWe may" \
               " disclose your Personal Information and certain information t" \
               "hat you provide to us or we collect from you as follows:\n\nWe do not sell email" \
               " addresses to third parties. You may voluntarily provide your" \
               " e-mail address at your option to other providers who have referral links to their " \
               "website from our Services.\n\nWe may share your Personal Info" \
               "rmation and Traffic Data with our business partners who perform core operational " \
               "services for SD (such as hosting, billing, fulfillment, data " \
               "storage, security, insurance verification, or Website analytics) and/or by making " \
               "certain features available to our users.\n\nWe may transfer y" \
               "our information to another company in connection with a merger, sale, acquisition" \
               " or other change of ownership or control by or of SD (whether" \
               " in whole or in part). Should one of these events occur, we will make reasonable " \
               "efforts to notify you before your information becomes subject" \
               " to different privacy and security policies and practices.\n\nWe also may need to " \
               "disclose your Personal Information or any other information w" \
               "e collect about you if we determine in good faith that such disclosure is needed " \
               "to: (1) comply with applicable law, regulation, court order o" \
               "r other legal process; (2) to prevent or lessen a serious and imminent threat to " \
               "the health or safety of you, another person or the public; (3" \
               ") enforce the Terms of Use with you; or (4) respond to claims that any posting or " \
               "other content violates third-party rights.\n\nWe may disclose" \
               " information that is not Personal Information that has been de-identified and aggregated)" \
               " at our discretion. We may also disclose de-identified usage " \
               "data to provide feedback on the Services.\n\n6. STORAGE AND SECURITY OF INFORMATION" \
               "\n\nWe store and process your information on our servers. We " \
               "maintain industry standard backup and archival systems.\n\nWe endeavor to follow generally" \
               " accepted industry standards to protect the Personal Informat" \
               "ion submitted to us, both during transmission and in storage." \
               " Although we make good faith efforts to store Personal Inform" \
               "ation in a secure operating environment that is not open to the public, " \
               "we do not and cannot guarantee the security of your Personal " \
               "Information. If we become aware that your Personal Information has been " \
               "disclosed in a manner not in accordance with this Privacy Pol" \
               "icy, we will use reasonable efforts to notify you of the nature and extent" \
               " of the disclosure (to the extent we know that information) a" \
               "s soon as reasonably possible and as permitted or required by law.\n\n" \
               "7. AMENDING YOUR PERSONAL INFORMATION\n\nIf you are a registe" \
               "red user of the Services, you may review and modify the information you " \
               "entered into your Personal Profile. You can modify your other" \
               " Personal Information, including your username and password, by accessing " \
               "the settings for your account.\n\nIf you wish to close your a" \
               "ccount, please email us at customerservice@sdcor.net. We will delete your " \
               "account and all of your Personal Information at your request " \
               "as soon as reasonably possible. Please know that SD does reserve the right" \
               " to retain certain information from closed accounts in order " \
               "to comply with law, prevent fraud, resolve disputes, enforce the Terms of" \
               " Use and take other actions permitted by law.\n\n8. CHANGES T" \
               "O THIS PRIVACY POLICY\n\nSD reserves the right to change the terms of this" \
               " Privacy Policy at any time. The process for changes to this " \
               "Privacy Policy are described in our Terms of Use. If we change the terms " \
               "of this Privacy Policy, the new terms will apply to all Perso" \
               "nal Information SD maintains, including information that was created or " \
               "received before such changes were made.\n\n9. CONTACTS\n\nIf " \
               "you have questions, concerns or comments regarding this Privacy Policy, " \
               "please contact us at customerservice@sdcor.net.\n\nSmart Diagnosis, Inc.\n\n"

    accept3 = ""
    accept3_ = ""
    emailAlert = "Your email address is invalid"
    pwAlert = "Password should be at least 6 characters. And #, <, >, (, ), |, ;, /, \\ cannot be used among special " \
              "characters. "
    pw2Alert = "Passwords do not match."
    notDuplicate = "'is available."
    isDuplicate = "An account already exist with the same email address."
    success = "Signup is complete."
    fail = "Signup failed"


class FindPWStr:
    success = "We send a link to reset your password to your email address."
    notMatch = "There is no user record corresponding to this email address."
    invalid = "Your email address is invalid."
    title = "  Find Password"
    email = "Email"
    alert = "Please enter your email."


class ResultStr:
    home_tab = "HOME"
    result_tab = "RESULT"
    change2ko = "한국어"
    change2en = "영어"
    result = "Results"
    rmssd = "RMSSD"
    ms = "ms"
    lf = "Low freq %"
    percent = "%"
    hf = "High freq %"
    stress = "Stress level"
    normal = "Normal"
    low = "Low"
    veryLow = "Very Low"
    high = "High"
    veryHigh = "Very High"
    sdnn = "SDNN"
    bpm_up = "BPM"
    bpm = "bpm"
    settings = "Settings"
    program = "program"
    makepdf = "Create a PDF file"
    logout = "Logout"
    close = "Exit"
    info = "CardiVu Info"
    help = "Help"
    start = "Start"
    stop = "Stop"
    info_ = "\nMAIL :\tmaxkim@sdcor.net\nTEL :\t+82-2-395-0327\nFAX :\t +82-2-395-0325\n\nCopyright ⓒ SMART DIAGNOSIS\n"

    day = "D"
    week = "W"
    month = "M"
    tab_range = "Period"
    e_date = "TO"
    s_date = "FROM"
    search = "Search"
    heart_rate_s = "심박수"
    heart_rate_t = "Heart Rate"
    hrv_s = "심박변이도"
    hrv_t = "Heart Rate Variability"
    sdnn_s = "심박동 변이성"
    sdnn_t = "SDNN*"
    rmssd_s = "부교감 신경 활성도"
    rmssd_t = "RMSSD*"
    lfhf_s = "교감/부교감 신경 반응"
    lfhf_t = "LF/HF*"
    hrv_exp = "*HF: Represents the response of the parasympathetic nerve, and is an indicator of mental and physical " \
              "stability and relaxation.\n*LF: indicates the response of the sympathetic nerve, an index indicating " \
              "tension and excitement\n*SDNN: Standard deviation of the heart rate interval, an index indicating the " \
              "ability of the autonomic nervous system to control the body\n*RMSSD: An index for grasping " \
              "parasympathetic regulatory capacity, stress index in the body, and resistance to stress\n" \
              "\nThe standard range is for reference only, and individual heart rate variability should be analyzed " \
              "based on the person's average value.\nThe higher the heart rate variability, the better the " \
              "psychological state, and the lower the tendency, the worse the psychological state. "
    stress_s = "스트레스 수준"
    stress_t = "Stress level"
    search_alert = "No data was retrieved."

    blink = "Eye closed"
    side_face = "Not front face"

    camera = "Camera is not connected.    "
    completeSave = "Completed creating PDF file"
    completeFail = "Failed creating PDF file"
