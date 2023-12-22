FROM python:3.9.18

WORKDIR /app

# RUN git clone https://github.com/cdps-etsit/practica_creativa2.git 
# RUN git clone https://github.com/tehedor/p3_calculadora_js_core.git

# RUN ls -la
# RUN ls -la p3_calculadora_js_core

COPY productpage ./
# COPY productpage /app/

# RUN ls -la practica_creativa2

# RUN cp p3_calculadora_js_core/config_page.py .
# RUN cp p3_calculadora_js_core/config_requirements.py .

# ENV GRUPO_NUMERO=09

# RUN python3 config_page.py
# RUN python3 config_requirements.py

RUN pip3 install -r requirements.txt

# RUN pip3 install testresources==2.0.1

EXPOSE 9080

CMD ["python3","productpage.py", "9080"]
# CMD ["python3","productpage_monolith.py", "9080"]