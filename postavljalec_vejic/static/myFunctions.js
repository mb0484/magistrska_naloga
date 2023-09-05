kolofonTextSlo = `
    <strong>Vejice 2.0</strong>
    <br/>Orodje za strojno postavljanje vejic
    <br/>Automated comma placement tool
    <br/>
    <br/><strong>Zbirka</strong>
    <br/>Orodja CJVT
    <br/>
    <br/><strong>Avtorji</strong>
    <br/>Martin Božič, Marko Robnik-Šikonja, Simon Krek, Špela Arhar Holdt, Iztok Kosem, Polona Gantar, Jaka Čibej, Kaja Dobrovoljc, Bojan Klemenc, Cyprian Laskowski
    <br/>
    <br/><strong>Izdelava spletnega vmesnika</strong>
    <br/>Martin Božič
    <br/>
    <br/><strong>Oblikovanje spletnega vmesnika</strong>
    <br/>Gašper Uršič, Gregor Makovec, Anže Jesenovec (Studio Kruh)
    <br/>
    <br/><strong>Izdajatelj</strong>
    <br/>Center za jezikovne vire in tehnologije, Univerza v Ljubljani
    <br/>Orodje je dostopno pod licenco GNU General Public License, različica 3
    <br/>
    <br/><strong>Citiranje</strong>
    <br/>Vejice 2.0, orodja.cjvt.si/vejice, dostop 26. 11. 2020.
`

kolofonTextAng = `
    <strong>Vejice 2.0</strong>
    <br/>Automated comma placement tool
    <br/>
    <br/>Online tool at orodja.cjvt.si
    <br/>CJVT Tools
    <br/>
    <br/>Ljubljana 2021
    <br/>
    <br/><strong>Authors</strong>
    <br/>Martin Božič, Marko Robnik-Šikonja, Simon Krek, Špela Arhar Holdt, Iztok Kosem, Polona Gantar, Jaka Čibej, Kaja Dobrovoljc, Bojan Klemenc, Cyprian Laskowski
    <br/>
    <br/><strong>Interface development</strong>
    <br/>Martin Božič
    <br/>
    <br/><strong>Interface design</strong>
    <br/>Gašper Uršič, Gregor Makovec, Anže Jesenovec (Studio Kruh)
    <br/>
    <br/><strong>Published by</strong>
    <br/>Centre for Language Resources and Technologies, University of Ljubljana
    <br/>
    <br/><strong>Licence</strong>
    <br/>This tool is licenced under GNU General Public License, version 3
    <br/>
    <br/><strong>Citation</strong>
    <br/>Vejice 2.0, Automated comma placement tool, orodja.cjvt.si/vejice, accessed on 26. 11. 2020.
`

vejicarDostopnostSlo = `
    Programska koda je dostopna v repozitoriju
    <a href="https://github.com/clarinsi/vejice" target="_blank">CLARIN.SI</a>.
    <br/><br/>To delo je dostopno pod licenco <br/>
    <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GNU General Public License, verzija 3</a>
`

vejicarDostopnostAng = `
    Source code is available at the
    <a href="https://github.com/clarinsi/vejice" target="_blank">CLARIN.SI</a> reporsitory.
    <br/><br/>This work is licensed under a <br/>
    <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GNU General Public License, version 3</a>
`

oOrodjuSlo = `
    Izhodiščna verzija orodja je bila izdelana v okviru diplomskega dela Martina Božiča “Globoke nevronske mreže za postavljanje vejic v slovenskem jeziku” na Fakulteti za računalništvo in informatiko UL, pod mentorstvom prof. Marka Robnika Šikonje. <br/><br/>Spletno orodje preverja postavitev vejic v slovenskih besedilih s pomočjo jezikovnega modela BERT, izpopolnjenega za problem postavljanja vejic. Za izpopolnjevanje modela je bila zgrajena učna množica iz dela besedil korpusa sodobne standardne slovenščine Gigafida 2.0. Učna množica je obsegala 907.870 stavkov, ki so v povprečju vsebovali vsak po dve vejici.<br/><br/>Orodje za strojno preverjanje postavitve vejic je zasnovano kot pomoč pri postavljanju vejic in ni nadomestek za lektorski pregled besedil. Orodje opozarja na manjkajoče vejice s sivo barvo in na odvečne vejice z modro barvo. Glede na teste program trenutno deluje uspešno v 96 odstotkih primerov.
`

oOrodjuAng = `
    The initial version of the tool was developed as part of diploma thesis by Martin Božič “Globoke nevronske mreže za postavljanje vejic v slovenskem jeziku” at the Faculty of Computer and Information Science, University of Ljubljana, mentored by prof. Marko Robnik Šikonja.
    <br/>
    <br/>Vejice online tool analyses the placement of commas in Slovene texts using BERT language model adapted for comma placement verification problem. For model upgrade, a new training data set was created comprising of a segment of the Gigafida corpus of standard modern Slovene 2.0. The data set consists of 907,870 sentences containing two commas per sentence on average. 
    <br/>
    <br/>The tool for automatic comma placement was developed with the aim to help users with comma placement, it does not replace professional manual proofreading or copy editing. In the tool, grey colour is used to indicate missing commas, redundant commas are marked by blue colour. Preliminary test showed that the tools performs with 94% accuracy.
`

publikacijeText = `
    BOŽIČ, Martin (avtor), ROBNIK ŠIKONJA, Marko (mentor). 
    <em>Globoke nevronske mreže za postavljanje vejic v slovenskem jeziku.
    </em> Diplomsko delo/naloga. Fakulteta za računalništvo in informatiko Univerze v Ljubljani.
    <br/>
    <a class="httpsBibliografija" href="https://repozitorij.uni-lj.si/Dokument.php?id=133688&lang=slv">https://repozitorij.uni-lj.si/Dokument.php?id=133688&lang=slv
    </a>
    <br/>
    <br/>ULČAR, Matej, ROBNIK ŠIKONJA, Marko. 
    <em>Finest BERT and CroSlo-Engual BERT: less is more in multilingual models.
    </em> arXiv preprint. 2020.
    <br/>
    <a class="httpsBibliografija" href="https://arxiv.org/abs/2006.07890 ">https://arxiv.org/abs/2006.07890
    </a>
    <br/>
    <br/>KREK, Simon, ARHAR HOLDT, Špela, ERJAVEC, Tomaž, ČIBEJ, Jaka, REPAR, Andraž, GANTAR, Polona, LJUBEŠIĆ, Nikola, KOSEM, Iztok, DOBROVOLJC, Kaja. 
    <em>Gigafida 2.0: The Reference Corpus of Written Standard Slovene.
    </em> V: Proceedings of the 12th Language Resources and Evaluation Conference" 2020. European Language Resources Association", str. 3340--3345".
    <br/>
    <a class="httpsBibliografija" href="https://www.aclweb.org/anthology/2020.lrec-1.409">https://www.aclweb.org/anthology/2020.lrec-1.409
    </a>
    <br/>
    <br/>HOLOZAN, Peter. Zbirka primerov rabe vejice Vejica 1.3. V: FIŠER, Darja (ur.), PANČUR, Andrej (ur.). 
    <em>Zbornik konference Jezikovne tehnologije in digitalna humanistika, 20.-21. september 2018, Ljubljana, Slovenija.
    </em> Ljubljana: Znanstvena založba Filozofske fakultete. 2018, str. 99–105. 
    <br/>
    <a class="httpsBibliografija" href="https://www.aclweb.org/anthology/2020.lrec-1.409">https://www.aclweb.org/anthology/2020.lrec-1.409
    </a>
`

const translations = {
    "title": ["Slovnični popravljalnik", "Slovnični popravljalnik"],
    "aboutPageTitle": ["O orodju", "About"],
    "changeLanguageTitle": ["English", "Slovenščina"],
    "postPlaceholderText": ["Prilepi ali vnesi besedilo", "Type or paste your text here"],
    "vstaviVzorcnoBesediloBtn": ["Vstavi vzorčno besedilo", "Insert sample text"],
    "potrdiBtn": ["Potrdi", "Save"],
    "cancelBtn": ["Prekliči", "Cancel"],
    "sendFeedbackInformationBtn": ["Pošlji povratne informacije", "Send us feedback information"],
    "pleaseWaitForResultInfo": ["Prosimo, počakajte na rezultat.", "Please wait for result"],
    "editModeEnableText": ["Urejanje omogočeno", "Edit mode enabled"],
    "editModeDisabledText": ["Urejanje onemogočeno", "Edit mode disabled"],
    "editModeCanceledText": ["Urejanje preklicano", "Edit mode canceled"],
    "editModeFinishedText": ["Urejanje končano", "Finished editing"],
    "copySuccessfulMessage": ["Kopiranje končano", "Copied"],
    "prenosViraFooter": ["Prenos vira", "Download"],
    "upravljanjeViraFooter": ["Upravljanje vira", "Provided by"],
    "infoOViruFooter": ["Informacije o viru", "Information"],
    "dostoponostViraFooter": ["Dostopnost vira", "Licence"],
    "cjvtTextFooter": ["Center za jezikovne vire in tehnologije", "Centre for Language Resources and Technologies"],
    "dostoponostViraTextFooter": ['To delo je dostopno pod licenco <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GNU General Public License, verzija 3</a>', 'This work is licensed under a <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GNU General Public License, version 3</a>'],
    //"dostoponostViraTextFooter": ['Delo je dostopno pod licenco <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>', 'This work is licensed under a <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>'],
    "kolofonText": [kolofonTextSlo, kolofonTextAng],
    "kolofonTitle": ['Kolofon <a href="about" class="btn-exit"><i class="material-icons" style="font-size: 1.6rem !important;">close</i></a>', 'Impressum <a href="about" class="btn-exit"><i class="material-icons" style="font-size: 1.6rem !important;">close</i></a>'],
    "kolofonBtn": ["Kolofon", "Impressum"],
    "arhivBtn": ["Arhiv različic", "Archive"],
    "repoVejiceBtn": ["Koda", "Source"],
    "vejiceNaslov": ["Vejice", "Commas"],
    "trenutnaRazlicicaNaslov": ["Trenutna različica", "Current version"],
    "licencaNaslov": ["Dostopnost", "Licence"],
    "vejicarDostopnost": [vejicarDostopnostSlo, vejicarDostopnostAng],
    "datumZadnjePosodobitve": ['Datum izdaje posodobitve: <br/>24. 2. 2021', 'Date of last update: <br/>24. 2. 2021'],
    "oOrodjuTitle": ["O orodju Vejice 2.0", "About Vejice 2.0"],
    "oOrodjuBesedilo": [oOrodjuSlo, oOrodjuAng],
    "publikcijeTitle": ["Publikacije", "Bibliography"],
    "pogojiUporabeTitle": ["Pogoji uporabe","Terms of use"],
    "pogojiUporabeText": [`
        Upravitelj orodja za postavljanje vejic, ki je javno dostopno na naslovu: <a href="https://orodja.cjvt.si/vejice/home">https://orodja.cjvt.si/vejice/home</a>, je Center za jezikovne vire in tehnologije Univerze v Ljubljani, 
        Fakulteta za računalništvo in informatiko, Večna pot 113, 1000 Ljubljana. Orodje za postavljanje vejic deluje tako, da uporabniki v prazno polje vnesejo besedilo po svoji izbiri in kliknejo na gumb, s katerim zaženejo orodje. 
        Tako dobijo besedilo s predlogi za odpravo napak pri postavitvi vejic. Orodje za postavljanje vejic je zasnovano kot pomoč pri postavljanju vejic in ni nadomestek za slovnico, pravopis ali lektorski pregled besedil. Upravitelj orodja ne odgovarja za morebitne nepravilnosti, ki so posledica uporabe orodja ali za kakršnokoli škodo, ki bi uporabnikom nastala zaradi nepravilnosti, ki so posledica avtomatizirane obdelave besedil s pomočjo orodja.
    `,`
        The application Vejice 2.0 (Automated comma placement tool) which is publicly accessible at: <a href="https://orodja.cjvt.si/vejice/home">https://orodja.cjvt.si/vejice/home</a> is operated by Centre for Language Resources and Technologies at the University of Ljubljana, Faculty of Computer and Information Science, Večna pot 113, 1000 Ljubljana, Slovenia  (hereinafter: CJVT). 
        Users may upload any text of their choice into the empty frame and click on the marked button. By clicking the button users initiate the tool to start its operation. The result of this procedure will be a text marked with suggestions for proper comma usage. 
        The application Vejice 2.0 (Automated comma placement tool) is conceived as a help tool for comma usage and is not a substitute for a grammar, spelling, proofreading or language editing. CJVT is not responsible for any mistakes or irregularities, which are suggested by the tool and shall not be liable in any way for damages arising from or cost incurred by the incorrect suggestions, which are the consequence of automatic processing of the texts uploaded into the tool.
    `],
    "soglasjeZaObdelavoTitle": ["Soglasje za hrambo besedil","Data processing consent"],
    "soglasjeZaObdelavoText": [`
        Uporabniki orodja za postavljanje vejic v aplikacijo vnašajo besedila prostovoljno in razumejo ter soglašajo s tem, da upravitelj orodja vnesena besedila lahko hrani in obdeluje, in sicer za potrebe 
        statistične in jezikovne analize delovanja orodja ter razvoja in izboljšav metodologije oziroma modela orodja. Če besedila, ki jih uporabniki vnesejo v orodje, vsebujejo osebne podatke, uporabniki z vnosom besedil soglašajo tudi s hrambo in obdelavo teh 
        osebnih podatkov, ki bodo uporabljeni zgolj za analizo in razvoj orodja za postavljanje vejic. Uporabniki, ki ne želijo hrambe in obdelave osebnih podatkov za namene analize in razvoja orodja za postavljanje vejic, naj pred vnosom besedila v orodje take podatke 
        odstranijo. Besedila, ki jih uporabniki vnesejo v orodje, bodo dostopna samo upravitelju orodja in osebam, ki ga razvijajo, ne bodo pa posredovana tretjim osebam ali dostopna javnosti. Vsa vnesena besedila upravitelj orodja lahko obdeluje in hrani do 3 leta, po preteku tega obdobja pa jih trajno izbriše.
    `,`
        Users of Vejice 2.0 (Automated comma placement tool) upload the texts into the tool voluntarily and understand and consent to processing and retention of such texts by CVTJ. CVTJ shall process and retain such texts solely for the purposes of statistical and linguistic analysis of the tool operation and for development and upgrades of methodology or operation model of the tool.
        By uploading the texts containing any personal data into the tool, users consent to retention and processing of such personal data, which shall only be used for analysis and further development of the tool. 
        Users who do not allow such retention and processing of personal data for the purposes of analysis and further development of the tool, shall remove any such data from the texts before uploading the texts into the tool.
        The texts uploaded into the tool by users shall only be available to CVTJ and to developers of the tool and shall not be transmitted to any third party and shall not be made available to the public.
        CVTJ may process and retain texts uploaded into the tool by users for up to 3 years from the moment of upload. After such period expires, CVTJ shall permanently delete all such texts.
    `],
    "arhivRazlicicTitle": [`
        Različice <a href="about" class="btn-exit"><i class="material-icons" style="font-size: 1.6rem !important;">close</i></a>
    `,`
        Versions <a href="about" class="btn-exit"><i class="material-icons" style="font-size: 1.6rem !important;">close</i></a>
    `],
    "arhivRazlicicText": [`
        Različica
        <br/><strong>Vejice 2.0</strong>
        <br/>
        <br/>
        Datum izdaje posodobitve: <strong>6.11.2022</strong>
    `,`
        Version
        <br/><strong>Commas 2.0</strong>
        <br/>
        <br/>
        Date of publication: <strong>6.11.2022</strong>
    `]
}

alertMessageSlo = `
    <strong>POGOJI UPORABE</strong>
    <br/>
    <br/>
    ${translations["pogojiUporabeText"][0]}
    <br/>
    <br/>
    <strong>SOGLASJE ZA OBDELAVO IN HRAMBO BESEDIL</strong>
    <br/>
    <br/>
    ${translations["soglasjeZaObdelavoText"][0]}
    <br/>
`

alertMessageSloTitle = "ORODJE ZA POSTAVLJANJE VEJIC"
alertMessageSloButton = "Strinjam se"
alertMessageSloTranslate = "English"

alertMessageAng = `
    <strong>TERMS OF USE</strong>
    <br/>
    <br/>
    ${translations["pogojiUporabeText"][1]}
    <br/>
    <br/>
    <strong>DATA PROCESSING CONSENT</strong>
    <br/>
    <br/>
    ${translations["soglasjeZaObdelavoText"][1]}
    <br/>
`

alertMessageAngTitle = "Vejice 2.0 Automated comma placement tool"
alertMessageAngButton = "Agree to terms"
alertMessageAngTranslate = "Slovenščina"

//0 -> Slovene, 1 -> English
let curPickedLanguage = 0

const manageOnPageLoad = async => {
    curPickedLanguageName = getCookie("pickedLanguage")
    if (curPickedLanguageName == "english") {
        curPickedLanguage = 1
    } else {
        curPickedLanguage = 0
    }

    translatePage();

    if (typeof potrdiBtn !== 'undefined' && typeof cancelBtn !== 'undefined') {
        potrdiBtn.style.visibility = "hidden";
        cancelBtn.style.visibility = "hidden";
    }

    setTimeout(function(){
        //check cookie
        var agreedToLegalNotice = getCookie("agreedToLegalNotice");

        // if (agreedToLegalNotice == "" || agreedToLegalNotice == "false") {
        //     functionAlert();
        // } 
    }, 1500);
}

const changePageTranslation = async => {
    if (curPickedLanguageName == "english") {
        curPickedLanguage = 0
        curPickedLanguageName = "slovene"
    } else {
        curPickedLanguage = 1
        curPickedLanguageName = "english"
    }
    setCookie("pickedLanguage", curPickedLanguageName, 360);

    translatePage()
}

const translatePage = async => {
    try {

        pageTitle.innerHTML = translations["title"][curPickedLanguage]
        aboutNavTitle.innerHTML = translations["aboutPageTitle"][curPickedLanguage]
        changeLanguageNavTitle.innerHTML = translations["changeLanguageTitle"][curPickedLanguage]
        prenosViraFooter.innerHTML = translations["prenosViraFooter"][curPickedLanguage]
        upravljanjeViraFooter.innerHTML = translations["upravljanjeViraFooter"][curPickedLanguage]
        infoOViruFooter.innerHTML = translations["infoOViruFooter"][curPickedLanguage]
        dostoponostViraFooter.innerHTML = translations["dostoponostViraFooter"][curPickedLanguage]
        cjvtTextFooter.innerHTML = translations["cjvtTextFooter"][curPickedLanguage]
        dostoponostViraTextFooter.innerHTML = translations["dostoponostViraTextFooter"][curPickedLanguage]
        if (typeof vstaviVzorcnoBesediloBtn !== 'undefined' && typeof post !== 'undefined' && typeof potrdiBtn !== 'undefined' && typeof cancelBtn !== 'undefined' && typeof sendFeedbackInformationBtn !== 'undefined') {
            vstaviVzorcnoBesediloBtn.innerHTML = translations["vstaviVzorcnoBesediloBtn"][curPickedLanguage]
            post.placeholder = translations["postPlaceholderText"][curPickedLanguage]
            potrdiBtn.innerHTML = translations["potrdiBtn"][curPickedLanguage]
            cancelBtn.innerHTML = translations["cancelBtn"][curPickedLanguage]
            sendFeedbackInformationBtn.innerHTML = translations["sendFeedbackInformationBtn"][curPickedLanguage]
        }
        if (typeof kolofonTitle !== 'undefined' && typeof kolofonText !== 'undefined' ) {
            kolofonTitle.innerHTML = translations["kolofonTitle"][curPickedLanguage]
            kolofonText.innerHTML = translations["kolofonText"][curPickedLanguage]
        }
        if (typeof kolofonBtn !== 'undefined' && vejiceNaslov !== 'undefined') {
            kolofonBtn.innerHTML = translations["kolofonBtn"][curPickedLanguage]
            arhivBtn.innerHTML = translations["arhivBtn"][curPickedLanguage]
            repoVejiceBtn.innerHTML = translations["repoVejiceBtn"][curPickedLanguage]
            vejiceNaslov.innerHTML = translations["vejiceNaslov"][curPickedLanguage]
            trenutnaRazlicicaNaslov.innerHTML = translations["trenutnaRazlicicaNaslov"][curPickedLanguage]
            licencaNaslov.innerHTML = translations["licencaNaslov"][curPickedLanguage]
            vejicarDostopnost.innerHTML = translations["vejicarDostopnost"][curPickedLanguage]
            datumZadnjePosodobitve.innerHTML = translations["datumZadnjePosodobitve"][curPickedLanguage]
            oOrodjuTitle.innerHTML = translations["oOrodjuTitle"][curPickedLanguage]
            oOrodjuBesedilo.innerHTML = translations["oOrodjuBesedilo"][curPickedLanguage]
            publikcijeTitle.innerHTML = translations["publikcijeTitle"][curPickedLanguage]
            pogojiUporabeTitle.innerHTML = translations["pogojiUporabeTitle"][curPickedLanguage]
            pogojiUporabeText.innerHTML = translations["pogojiUporabeText"][curPickedLanguage]
            soglasjeZaObdelavoTitle.innerHTML = translations["soglasjeZaObdelavoTitle"][curPickedLanguage]
            soglasjeZaObdelavoText.innerHTML = translations["soglasjeZaObdelavoText"][curPickedLanguage]
        }
        if (typeof arhivRazlicicTitle !== 'undefined' && arhivRazlicicText !== 'undefined') {
            arhivRazlicicTitle.innerHTML = translations["arhivRazlicicTitle"][curPickedLanguage]
            arhivRazlicicText.innerHTML = translations["arhivRazlicicText"][curPickedLanguage]
        }
    } catch {}
}

function translateLegalNoticeWindow() {
    console.log(curPickedLanguage)
    if (curPickedLanguage == 0) {
        document.getElementById("alertMessageTitle").innerHTML = alertMessageSloTitle;
        document.getElementById("alertMessage").innerHTML = alertMessageSlo;
        document.getElementById("alertMessageButton").innerHTML = alertMessageSloButton;
        document.getElementById("alertMessageTranslate").innerHTML = alertMessageSloTranslate;
    } else {
        document.getElementById("alertMessageTitle").innerHTML = alertMessageAngTitle;
        document.getElementById("alertMessage").innerHTML = alertMessageAng;
        document.getElementById("alertMessageButton").innerHTML = alertMessageAngButton;
        document.getElementById("alertMessageTranslate").innerHTML = alertMessageAngTranslate;
    }
}

function functionAlert(myYes) {
    try {
        dimmAppBackground();
    } catch {}

    translateLegalNoticeWindow();

    var confirmBox = $("#confirm");
    confirmBox.find(".agreeLink").unbind().click(function() {
       confirmBox.hide();
       setCookie("agreedToLegalNotice", true, 360);
       cancelDimmAppBackground();
       translatePage();
    });
    confirmBox.find(".translateLegalNotice").unbind().click(function() {
        curPickedLanguageName = getCookie("pickedLanguage")
        if (curPickedLanguageName == "english") {
            curPickedLanguage = 0
            curPickedLanguageName = "slovene"
        } else {
            curPickedLanguage = 1
            curPickedLanguageName = "english"
        }
        setCookie("pickedLanguage", curPickedLanguageName, 360);
        translateLegalNoticeWindow();
    });
    confirmBox.find(".agreeLink").click(myYes);
    confirmBox.show();
 }

const dimmAppBackground = async => {
    document.getElementById("wholeView").classList.add("dimmBackground");
    document.getElementById("footerView").classList.add("dimmBackground");
}

const cancelDimmAppBackground = async => {
    document.getElementById("wholeView").classList.remove("dimmBackground");
    document.getElementById("footerView").classList.remove("dimmBackground");
}

let countDownTimerCopiedText = 0
let curMarkedNotEditedText = ""

const vzorcnoBesedilo = "Napake, ki jo slovnični popravljalnik, uspešno popravi so označene s rdeco barvo, napake, katerh pa ne uspe popravit, pa z rumeno brvivavo."

const clearText = async => {
    document.getElementById("charactersCount").innerHTML = "0/3000"
    document.getElementById("post").value = ""
}

const vstaviVzorcnoBesedilo = async => {
    document.getElementById("post").value = vzorcnoBesedilo
}

const postaviVejice = async => {
    if (document.getElementById("post").value.length > 0) {
    document.getElementById("likeButton").src = src="static/assets/thumbs-up.svg";
    document.getElementById("dislikeButton").src = src="static/assets/thumbs-down.svg";

    document.getElementById("markedTextField").textContent = translations["pleaseWaitForResultInfo"][curPickedLanguage];
    }
}

const editMarkedText = async => {
    const contentEditable = document.getElementById("markedTextField").isContentEditable
    if (!contentEditable) {
        countDownTimerCopiedText = 4
        copySuccessful.innerHTML = translations["editModeEnableText"][curPickedLanguage]
        copySuccessful.style.visibility = "visible";

        likeButton.style.visibility = "hidden";
        dislikeButton.style.visibility = "hidden";
        editTextBtn.style.visibility = "hidden";
        copyTextBtn.style.visibility = "hidden";
        //shareTextBtn.style.visibility = "hidden";
        potrdiBtn.style.visibility = "visible";
        cancelBtn.style.visibility = "visible";

        curMarkedNotEditedText = document.getElementById("markedTextField").innerHTML
    }
    else {
        countDownTimerCopiedText = 4
        copySuccessful.innerHTML = translations["editModeDisabledText"][curPickedLanguage]
        copySuccessful.style.visibility = "visible";
    }
    document.getElementById("markedTextField").setAttribute("contenteditable", true);
}

const cancelMarkedTextEdit = async => {
    countDownTimerCopiedText = 4
    copySuccessful.innerHTML = translations["editModeCanceledText"][curPickedLanguage]
    copySuccessful.style.visibility = "visible";

    likeButton.style.visibility = "visible";
    dislikeButton.style.visibility = "visible";
    editTextBtn.style.visibility = "visible";
    copyTextBtn.style.visibility = "visible";
    //shareTextBtn.style.visibility = "visible";
    potrdiBtn.style.visibility = "hidden";
    cancelBtn.style.visibility = "hidden";

    document.getElementById("markedTextField").innerHTML = curMarkedNotEditedText
    document.getElementById("markedTextField").setAttribute("contenteditable", false);
}

const confirmMarkedTextEdit = async => {
    countDownTimerCopiedText = 4
    copySuccessful.innerHTML = translations["editModeFinishedText"][curPickedLanguage]
    copySuccessful.style.visibility = "visible";

    likeButton.style.visibility = "visible";
    dislikeButton.style.visibility = "visible";
    editTextBtn.style.visibility = "visible";
    copyTextBtn.style.visibility = "visible";
    //shareTextBtn.style.visibility = "visible";
    potrdiBtn.style.visibility = "hidden";
    cancelBtn.style.visibility = "hidden";

    curMarkedNotEditedText = document.getElementById("markedTextField").innerHTML
    document.getElementById("markedTextField").setAttribute("contenteditable", false);
}

const updateLength = async => {
    document.getElementById("charactersCount").innerHTML = document.getElementById("post").value.length + "/3000"
}

const likeCurrentMarkedText = async(markedTextId) => {
    if (markedTextId && markedTextId != -1) {
        $.ajax({
            url: 'likeDislikeMarkedText',    //Your api url
            type: 'PUT',   //type is any HTTP method
            data: {
                markedTextId: markedTextId,
                textScore: 1
            },      //Data as js object
            success: function () {
                document.getElementById("likeButton").src = src="static/assets/thumbs-up-filled.png";
                document.getElementById("dislikeButton").src = src="static/assets/thumbs-down.svg";
            }
        });
    }
    else if (markedTextId == -1) {
        document.getElementById("likeButton").src = src="static/assets/thumbs-up-filled.png";
        document.getElementById("dislikeButton").src = src="static/assets/thumbs-down.svg";
    }
}

const dislikeCurrentMarkedText = async(markedTextId) => {
    if (markedTextId && markedTextId != -1) {
        $.ajax({
            url: 'likeDislikeMarkedText',    //Your api url
            type: 'PUT',   //type is any HTTP method
            data: {
                markedTextId: markedTextId,
                textScore: -1
            },      //Data as js object
            success: function () {
                document.getElementById("likeButton").src = src="static/assets/thumbs-up.svg";
                document.getElementById("dislikeButton").src = src="static/assets/thumbs-down-filled.png";
            }
        });
    }
    else if (markedTextId == -1) {
        document.getElementById("likeButton").src = src="static/assets/thumbs-up.svg";
        document.getElementById("dislikeButton").src = src="static/assets/thumbs-down-filled.png";
    }
}

window.setInterval(function(){
    try {
    document.getElementById("charactersCount").innerHTML = document.getElementById("post").value.length + "/3000"
    }
    catch {}

    if (countDownTimerCopiedText > 0) {
        countDownTimerCopiedText -= 1
    if (countDownTimerCopiedText == 0) {
        copySuccessful.style.visibility = "hidden";
    }
    }

}, 500);

// function copyMarkedText() {
//     if (document.getElementById("markedTextField").innerHTML.length > 0) {
//     var target = document.getElementById('markedTextField');
//     var range, select;
//     if (document.createRange) {
//         range = document.createRange();
//         range.selectNode(target)
//         select = window.getSelection();
//         select.removeAllRanges();
//         select.addRange(range);
//         document.execCommand('copy');
//         select.removeAllRanges();
//     } else {
//         range = document.body.createTextRange();
//         range.moveToElementText(target);
//         range.select();
//         document.execCommand('copy');
//     }
//     countDownTimerCopiedText = 4
//     copySuccessful.innerHTML = translations["copySuccessfulMessage"][curPickedLanguage]
//     copySuccessful.style.visibility = "visible";
//     }
// }

function copyMarkedText() {
    if (document.getElementById("markedTextField").innerHTML.length > 0) {
        var target = document.getElementById('markedTextField');
        var markedText = target.textContent; // Get the concatenated text content from all divs

        // Excluding text from <div class="select-option">
        var optionDivs = target.querySelectorAll(".select-option");
        optionDivs.forEach(function(optionDiv) {
            //console.log("optionDiv: ", optionDiv)
            //console.log("optionDiv.textContent: ", optionDiv.textContent)
            markedText = markedText.replaceAll(" " + optionDiv.textContent + " ", "ksdjhglkdfjhglkjh");

            markedText = markedText.replaceAll(" " + optionDiv.textContent + ",", "ksdjhgl,kdfjhglkjh");
            markedText = markedText.replaceAll(" " + optionDiv.textContent + ".", "ksdjhgl.kdfjhglkjh");
            markedText = markedText.replaceAll(" " + optionDiv.textContent + ")", "ksdjhgl)kdfjhglkjh");

            markedText = markedText.replace(optionDiv.textContent, "");
            markedText = markedText.replaceAll("ksdjhglkdfjhglkjh", " " + optionDiv.textContent + " ");

            markedText = markedText.replaceAll("ksdjhgl,kdfjhglkjh", " " + optionDiv.textContent + ",");
            markedText = markedText.replaceAll("ksdjhgl.kdfjhglkjh", " " + optionDiv.textContent + ".");
            markedText = markedText.replaceAll("ksdjhgl)kdfjhglkjh", " " + optionDiv.textContent + ")");

            //console.log("markedText: ", markedText)
        });

        var dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
        dummy.value = markedText.trim(); // Trim any leading/trailing whitespace
        dummy.select();
        document.execCommand('copy');
        document.body.removeChild(dummy);
        countDownTimerCopiedText = 4;
        copySuccessful.innerHTML = translations["copySuccessfulMessage"][curPickedLanguage];
        copySuccessful.style.visibility = "visible";
    }
}

function openTwitter() {
    window.open("https://twitter.com/share?url="+encodeURIComponent(window.location.href)+"&text="+document.title+'&hashtags=cjvt,vejice', '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600');return false;
};

$(document).on('click touch','#share-fb',function() {
    window.open(
            'https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(window.location.href)+"&fbrefresh=true",
            'facebook-share-dialog',
            'width=626,height=436');
    return false;
});

/* manage about page grid - novi design about page */

//basic - 0, oOrodju - 1, kolofon - 2, bibliografija - 3
var curStateGrid = 0

naslovOOrodju = "O orodju"
textOOrodjuKrajse = "Izhodiščna verzija orodja je bila izdelana v okviru diplomskega dela Martina Božiča “Globoke nevronske mreže za postavljanje vejic v slovenskem jeziku” na Fakulteti za računalništvo in informatiko UL, pod mentorstvom prof. Marka Robnika Šikonje."
textOOrodju = "Izhodiščna verzija orodja je bila izdelana v okviru diplomskega dela Martina Božiča “Globoke nevronske mreže za postavljanje vejic v slovenskem jeziku” na Fakulteti za računalništvo in informatiko UL, pod mentorstvom prof. Marka Robnika Šikonje. <br/><br/>Spletno orodje preverja postavitev vejic v slovenskih besedilih s pomočjo jezikovnega modela BERT, izpopolnjenega za problem postavljanja vejic. Za izpopolnjevanje modela je bila zgrajena učna množica iz dela besedil korpusa sodobne standardne slovenščine Gigafida 2.0. Učna množica je obsegala 907.870 stavkov, ki so v povprečju vsebovali vsak po dve vejici.<br/><br/>Orodje za strojno preverjanje postavitve vejic je zasnovano kot pomoč pri postavljanju vejic in ni nadomestek za lektorski pregled besedil. Orodje opozarja na manjkajoče vejice s sivo barvo in na odvečne vejice z modro barvo. Glede na teste program trenutno deluje uspešno v 96 odstotkih primerov."
gumbOOrodju = "Več o orodju"

naslovVejice = "Vejice"
textVejiceKrajse = "Orodje za strojno postavljanje vejic<br/>Automated comma placement tool"
textVejice = "<strong>Vejice 2.0</strong><br/>Orodje za strojno postavljanje vejic<br/>Automated comma placement tool<br/><br/><strong>Zbirka</strong><br/>Orodja CJVT<br/><br/><strong>Avtorji</strong><br/>Martin Božič, Marko Robnik-Šikonja, Simon Krek, Špela Arhar Holdt, Iztok Kosem, Polona Gantar, Jaka Čibej, Kaja Dobrovoljc, Bojan Klemenc, Cyprian Laskowski<br/><br/><strong>Izdelava spletnega vmesnika</strong><br/>Martin Božič<br/><br/><strong>Oblikovanje spletnega vmesnika</strong><br/>Gašper Uršič, Gregor Makovec, Anže Jesenovec (Studio Kruh)<br/><br/><strong>Izdajatelj</strong><br/>Center za jezikovne vire in tehnologije, Univerza v Ljubljani<br/>Orodje je dostopno pod licenco GNU General Public License, različica 3<br/><br/><strong>Citiranje</strong><br/>Vejice 2.0, orodja.cjvt.si/vejice, dostop 26. 11. 2020."
gumbVejice = "Kolofon"

naslovTrenutnaRazlicica = "Trenutna različica"
textTrenutnaRazlicicaKrajse = "Trenutna različica orodja je 2.0.<br/>datum izdaje posodobitve: 22. 10. 2019"
textTrenutnaRazlicica = ""
gumbTrenutnaRazlicica = "Arhiv različic"

naslovDostoponost = "Dostoponost"
textDostoponostKrajse = "Baza slovarja je dostopna v repozitoriju Clarin.Si.<br/>To delo je dostopno pod licenco Creative Commons Priznanje avtorstva<br/>Deljenje pod enakimi pogoji 4.0."
textDostoponost = ""
gumbDostoponost = "Baza slovarja"

naslovBibliografija = "Bibliografija"
textBibliografijaKrajse = "Seznam povezanih bibliotekarskih virov, uporabljenih pri zasnovi uporabniškega vmesnika Vejice 2.0"
textBibliografija = 'BOŽIČ, Martin (avtor), ROBNIK ŠIKONJA, Marko (mentor). <em>Globoke nevronske mreže za postavljanje vejic v slovenskem jeziku.</em> Diplomsko delo/naloga. Fakulteta za računalništvo in informatiko Univerze v Ljubljani.<br/><a class="httpsBibliografija" href="https://repozitorij.uni-lj.si/Dokument.php?id=133688&lang=slv">https://repozitorij.uni-lj.si/Dokument.php?id=133688&lang=slv</a><br/><br/>ULČAR, Matej, ROBNIK ŠIKONJA, Marko. <em>Finest BERT and CroSlo-Engual BERT: less is more in multilingual models.</em> arXiv preprint. 2020.<br/><a class="httpsBibliografija" href="https://arxiv.org/abs/2006.07890 ">https://arxiv.org/abs/2006.07890</a><br/><br/>KREK, Simon, ARHAR HOLDT, Špela, ERJAVEC, Tomaž, ČIBEJ, Jaka, REPAR, Andraž, GANTAR, Polona, LJUBEŠIĆ, Nikola, KOSEM, Iztok, DOBROVOLJC, Kaja. <em>Gigafida 2.0: The Reference Corpus of Written Standard Slovene.</em> V: Proceedings of the 12th Language Resources and Evaluation Conference" 2020. European Language Resources Association", str. 3340--3345".<br/><a class="httpsBibliografija" href="https://www.aclweb.org/anthology/2020.lrec-1.409">https://www.aclweb.org/anthology/2020.lrec-1.409</a><br/><br/>HOLOZAN, Peter. Zbirka primerov rabe vejice Vejica 1.3. V: FIŠER, Darja (ur.), PANČUR, Andrej (ur.). <em>Zbornik konference Jezikovne tehnologije in digitalna humanistika, 20.-21. september 2018, Ljubljana, Slovenija.</em> Ljubljana: Znanstvena založba Filozofske fakultete. 2018, str. 99–105. <br/><a class="httpsBibliografija" href="https://www.aclweb.org/anthology/2020.lrec-1.409">https://www.aclweb.org/anthology/2020.lrec-1.409</a>'
gumbBibliografija = "Seznam virov"

naslovVprasanja = "Vprašanja"
textVprasanjaKrajse = "Za vsa dodatna vprašanja se obrnite na kontaktni center, nam pišite na <br/>info@cjvt.si ali nas pokličite na 031-887-395 (Drago Mije)."
textVprasanja = ""
gumbVprasanja = "Dodatna vprašanja"


$(document).on('click touch','#aboutContainerOpen11', function() {
    prikaziKolofon();
    return false
});

$(document).on('click touch','#aboutContainerOpen13', function() {
    prikaziOOrodju();
    return false
});

$(document).on('click touch','#aboutContainerOpen23', function() {
    if (curStateGrid == 0) {
        prikaziBibliografijo();
    } else if (curStateGrid == 2) {
        prikaziOOrodju();
    }
    return false
});

$(document).on('click touch','#aboutContainerOpen21', function() {
    if (curStateGrid == 1 || curStateGrid == 3) {
        prikaziKolofon();
    }
    return false
});

$(document).on('click touch','#aboutContainerOpen24', function() {
    if (curStateGrid == 1 || curStateGrid == 2) {
        prikaziBibliografijo();
    } else if (curStateGrid == 3) {
        prikaziOOrodju();
    }
    return false
});

//prikazi kolofon
function prikaziKolofon() {
    curStateGrid = 2
    //left
    document.getElementById("aboutContainer0").classList.remove("hidden");
    aboutContainerTitle0.innerHTML = naslovVejice
    aboutContainerText0.innerHTML = textVejice

    document.getElementById("aboutContainer11").classList.add("hidden");
    document.getElementById("aboutContainer12").classList.add("hidden");
    document.getElementById("aboutContainer13").classList.add("hidden");
    //right
    aboutContainerTitle21.innerHTML = naslovTrenutnaRazlicica
    aboutContainerText21.innerHTML = textTrenutnaRazlicicaKrajse
    aboutContainerOpen21.innerHTML = gumbTrenutnaRazlicica

    aboutContainerTitle22.innerHTML = naslovDostoponost
    aboutContainerText22.innerHTML = textDostoponostKrajse
    aboutContainerOpen22.innerHTML = gumbDostoponost

    aboutContainerTitle23.innerHTML = naslovOOrodju
    aboutContainerText23.innerHTML = textOOrodjuKrajse
    aboutContainerOpen23.innerHTML = gumbOOrodju

    document.getElementById("aboutContainer24").classList.remove("hidden");
    aboutContainerTitle24.innerHTML = naslovBibliografija
    aboutContainerText24.innerHTML = textBibliografijaKrajse
    aboutContainerOpen24.innerHTML = gumbBibliografija
    $("html, body").animate({ scrollTop: 0 }, "slow");
};

//prikazi bibliografija
function prikaziBibliografijo() {
    curStateGrid = 3
    //left
    document.getElementById("aboutContainer0").classList.remove("hidden");
    aboutContainerTitle0.innerHTML = naslovBibliografija
    aboutContainerText0.innerHTML = textBibliografija

    document.getElementById("aboutContainer11").classList.add("hidden");
    document.getElementById("aboutContainer12").classList.add("hidden");
    document.getElementById("aboutContainer13").classList.add("hidden");
    //right
    aboutContainerTitle21.innerHTML = naslovVejice
    aboutContainerText21.innerHTML = textVejiceKrajse
    aboutContainerOpen21.innerHTML = gumbVejice

    aboutContainerTitle22.innerHTML = naslovTrenutnaRazlicica
    aboutContainerText22.innerHTML = textTrenutnaRazlicicaKrajse
    aboutContainerOpen22.innerHTML = gumbTrenutnaRazlicica

    aboutContainerTitle23.innerHTML = naslovDostoponost
    aboutContainerText23.innerHTML = textDostoponostKrajse
    aboutContainerOpen23.innerHTML = gumbDostoponost

    document.getElementById("aboutContainer24").classList.remove("hidden");
    aboutContainerTitle24.innerHTML = naslovOOrodju
    aboutContainerText24.innerHTML = textOOrodjuKrajse
    aboutContainerOpen24.innerHTML = gumbOOrodju
    $("html, body").animate({ scrollTop: 0 }, "slow");
};

//prikazi o orodju
function prikaziOOrodju() {
    curStateGrid = 1
    //left
    document.getElementById("aboutContainer0").classList.remove("hidden");
    aboutContainerTitle0.innerHTML = naslovOOrodju
    aboutContainerText0.innerHTML = textOOrodju

    document.getElementById("aboutContainer11").classList.add("hidden");
    document.getElementById("aboutContainer12").classList.add("hidden");
    document.getElementById("aboutContainer13").classList.add("hidden");
    //right
    aboutContainerTitle21.innerHTML = naslovVejice
    aboutContainerText21.innerHTML = textVejiceKrajse
    aboutContainerOpen21.innerHTML = gumbVejice

    aboutContainerTitle22.innerHTML = naslovTrenutnaRazlicica
    aboutContainerText22.innerHTML = textTrenutnaRazlicicaKrajse
    aboutContainerOpen22.innerHTML = gumbTrenutnaRazlicica

    aboutContainerTitle23.innerHTML = naslovDostoponost
    aboutContainerText23.innerHTML = textDostoponostKrajse
    aboutContainerOpen23.innerHTML = gumbDostoponost

    document.getElementById("aboutContainer24").classList.remove("hidden");
    aboutContainerTitle24.innerHTML = naslovBibliografija
    aboutContainerText24.innerHTML = textBibliografijaKrajse
    aboutContainerOpen24.innerHTML = gumbBibliografija
    $("html, body").animate({ scrollTop: 0 }, "slow");
};


// manage cookies

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    console.log(exdays)
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    console.log(d.toUTCString())
    var expires = "Expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}


function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');

    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }

    return "";
}

document.addEventListener('DOMContentLoaded', function() {
    const collection = document.getElementsByClassName('select-container');

    for (selectContainer of collection) {

        selectContainer.addEventListener('click', function(event) {
            var id = event.target.id.split('&')[1]

            var selectOptions = document.getElementById('select-options&' + id);
            var selectContainer = document.getElementById('selectContainer&' + id);
            var text = document.getElementById('text&' + id);
            console.log("selectOptions: ", selectOptions)

            selectOptions.style.display = 'block';
            var change = false

            document.addEventListener('click', function(event) {
                if (change || !selectContainer.contains(event.target)) {
                    selectOptions.style.display = 'none';
                    change = false
                }
            });

            selectOptions.addEventListener('click', function(event) {
                change = true
                var clickedWord = event.target.textContent;
                text.innerHTML = clickedWord;
            });
        });
    }
});