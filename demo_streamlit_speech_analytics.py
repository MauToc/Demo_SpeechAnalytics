import streamlit as st
import time

##########
# File Input
##########
#conversation_01_abnormal call drop.txt: (qui di un problema sulla fornitura del gas e poi alla fine cade la chiamata).
    # kpi trovati: abonormal call drop; opening (ovvero se l'operatore si presenta al cliente)
#conversation_02_upselling.txt: (qui l'operatore prova a afare upselling):
    # kpi trovati: upselling; opening; dati cliente
#conversation_03_incorrect_behavior.txt: (qui l'operatore tiene un comportamento scorretto dicendo che non è un suo problema, per altro non fa nemmeno l'opening).
    # kpi trovati: incorrect behavior
#conversation_04_customer_data.txt: (qui l'operatore chiede i dati del cliente come nome, cognome, indirizzo, tessera sanitaria, iban, ecc, per fare una nuova attivazione):
    # kpi trovati: customer data; opening


##########
# Caricamento Immagini Header e Sidebar
##########
st.sidebar.image("../img/sidebar.png", use_column_width=True)
st.image('../img/header.png')#, use_column_width=True)#, caption='Descrizione dell\'immagine')


##########
# Pulsante per fare browse di file da una cartella
##########
uploaded_file = st.file_uploader("")


pallini=0
if uploaded_file is not None:
    progress_bar = st.progress(0)

    ##########
    # Caricamento trascrizione
    ##########
    if uploaded_file.type == "text/plain":
        file_content = uploaded_file.read().decode("utf-8")

        centered_text_html = """
        <div style="text-align: center; font-weight: bold; font-size: 14px; font-family: Arial;">
            TRANSCRIPTION
        </div>
        """
        # Display the centered text
        st.markdown(centered_text_html, unsafe_allow_html=True)

        ##########
        # Barra di caricamento trascrizione
        ##########
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        #st.success("Loaded!")

        st.text_area("", file_content, height=200)
        pallini=1
    else:
        st.warning("")
else:
    st.info("")


##########
# Mostrare i KPI
##########
if pallini==1:

    #Ogni elemento della lista principale è riferito (in ordine) ad una conversazione (01,02,03,04)
    #Ogni elemento delle sottoliste è riferito alla presenza (green) o non presenza (red) di un KPI
    #L'ordine dei kpi nelle sottoliste è: opening, upselling, customer data, abnormal_drop, incorrect_behavior
    colori=[['green','red','red','green','red'], #conv01 - KPI: opening, abonormal call drop
            ['green','green','green','red','red'], #conv02 - KPI: opening, upselling, customer data
            ['red','red','red','red','green'], #conv03 - KPI: incorrect behavior
            ['green','red','green','red','red']] #conv04 - KPI: opening, customer data

    #conversation_01_abnormal call drop
    #problema sulla fornitura del gas e poi alla fine cade la chiamata
    if "Conversation01" in file_content: #KPI: opening, abonormal call drop
         c=0
    
    #conversation_02_upselling
    #l'operatore prova a afare upselling
    if "Conversation02" in file_content: #KPI: opening, upselling, customer data
         c=1
    
    #conversation_03_incorrect_behavior
    #l'operatore tiene un comportamento scorretto (non è un mio problema); non fa nemmeno l'opening
    if "Conversation03" in file_content: #KPI: incorrect behavior
         c=2
    
    #conversation_04_customer_data
    #l'operatore chiede i dati del cliente (nome, cognome, indirizzo, ecc) per una nuova attivazione
    if "Conversation04" in file_content: #KPI: opening, customer data
         c=3
    
    # Aggiungi un po' di spazio verticale
    st.markdown("<br>", unsafe_allow_html=True)

    ##########
    # Caricamento analisi KPI
    ##########
    progress_bar = st.progress(0)
    for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        #st.success("Loaded!")


    ##########
    # Report KPI (single)
    ##########
    centered_text_html = """
    <div style="text-align: center; font-weight: bold; font-size: 14px; font-family: Arial;">
        KPI REPORT (single)
    </div>
    """
    # Display the centered text
    st.markdown(centered_text_html, unsafe_allow_html=True)

    # Disegna un pallino per il KPI_1 (opening)
    st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <div style="width: 20px; height: 20px; background-color:{colori[c][0]}; border-radius: 50%; margin-right: 10px;"></div>
            <span>KPI: opening</span>
        </div>
    """, unsafe_allow_html=True)

    # Aggiungi un po' di spazio verticale
    #st.markdown("<br>", unsafe_allow_html=True)

    # Disegna un pallino per il KPI_2 (upselling)
    st.markdown(f"""     
        <div style="display: flex; align-items: center;">
            <div style="width: 20px; height: 20px; background-color:{colori[c][1]}; border-radius: 100%; margin-right: 10px;"></div>
            <span>KPI: upselling</span>
        </div>
    """, unsafe_allow_html=True)

    # Disegna un pallino per il KPI_3 (customer data)
    st.markdown(f"""     
        <div style="display: flex; align-items: center;">
            <div style="width: 20px; height: 20px; background-color:{colori[c][2]}; border-radius: 100%; margin-right: 10px;"></div>
            <span>KPI: customer data</span>
        </div>
    """, unsafe_allow_html=True)


    # Disegna un pallino per il KPI_4 (abnormal call drop)
    st.markdown(f"""     
        <div style="display: flex; align-items: center;">
            <div style="width: 20px; height: 20px; background-color:{colori[c][3]}; border-radius: 100%; margin-right: 10px;"></div>
            <span>KPI: abnormal call drop</span>
        </div>
    """, unsafe_allow_html=True)




    # Disegna un pallino per il KPI_5 (incorrect operator behavior)
    st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <div style="width: 20px; height: 20px; background-color:{colori[c][4]}; border-radius: 50%; margin-right: 10px;"></div>
            <span>KPI: incorrect behavior</span>
        </div>
    """, unsafe_allow_html=True)

    #st.markdown("<br>", unsafe_allow_html=True)

    #st.write("KPI Report (overall)")

    # Aggiungi un po' di spazio verticale
    st.markdown("<br>", unsafe_allow_html=True)

    ##########
    # Report KPI (overall)
    ##########
    centered_text_html = """
    <div style="text-align: center; font-weight: bold; font-size: 14px; font-family: Arial;">
        KPI REPORT (overall)
    </div>
    """
    # Display the centered text
    st.markdown(centered_text_html, unsafe_allow_html=True)
  
  # Define styles for the table
    table_styles = """
    <style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid black;
        text-align: center;
        padding: 10px;
    }
    th {
        font-weight: bold;
    }
    </style>
    """
    
    # Display the table styles
    st.markdown(table_styles, unsafe_allow_html=True)

    # Define the HTML for the table
    table_html = """
    <table>
        <tr>
            <th>Opening</th>
            <th>Upselling</th>
            <th>Customer Data</th>
            <th>Abnormal Call Drop</th>
            <th>Incorrect Behavior</th>
        </tr>
        <tr>
            <td>80%</td>
            <td>25%</td>
            <td>40%</td>
            <td>25%</td>
            <td>25%</td>
        </tr>
    </table>
    """

    # Mostra il contenuto HTML nella pagina
    st.markdown(table_html, unsafe_allow_html=True) 