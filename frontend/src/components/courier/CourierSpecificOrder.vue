<template>
  <v-container>
    <v-row justify="center">
      <h1 class="text-center mb-4">Заказ #{{ order.id }}</h1>
    </v-row>

    <v-stepper v-if="!success" v-model="e13" vertical>
      <v-stepper-step step="1" :complete="step1Complete"
        >Шаг 1. Доберитесь до заказчика</v-stepper-step
      >

      <v-stepper-content step="1">
        <v-card class="mb-12" height="300px">
          <MapTwoDots :from="order.pointFrom"></MapTwoDots>
        </v-card>
        <v-btn color="primary" @click="finishStep1">
          Подтвердить встречу с заказчиком
        </v-btn>
      </v-stepper-content>

      <v-stepper-step step="2" :complete="step2Complete">
        Шаг 2. Подтвердите передачу посылки и оставьте подпись
      </v-stepper-step>

      <v-stepper-content step="2">
        <v-card color="" class="mb-12">
          <v-btn
            class="mb-5"
            color="dark"
            dark
            @click="openModalStep2()"
            v-if="!signatureSaved"
          >
            Нажмите и распишитесь
          </v-btn>
          <div v-else>
            <h4>Подпись курьера</h4>
            <img height="300" :src="base64img" alt="" /><br />
            <v-btn class="mb-5" text @click="retry()">
              Повторить процедуру
            </v-btn>
          </div>

          <v-dialog v-model="dialogStep2" width="500">
            <v-card>
              <v-card-title class="text-h5 grey lighten-2">
                Пожалуйста, оставьте подпись
              </v-card-title>

              <v-card-text class="mt-2 pb-0">
                Оставляя подпись, вы подтверждаете получение посылки от
                заказчика
              </v-card-text>
              <v-container fluid>
                <h2>Распишитесь в окошке ниже и сохраните подпись в системе</h2>
                <canvas id="canvasStep2"></canvas><br />
                <v-btn text @click="signatureSavePng">
                  Сохранить как png
                </v-btn>
                <v-btn text @click="signatureClear"> Очистить </v-btn><br />
                <v-btn @click="signatureSaveInDbStep2"
                  >Сохранить подпись в системе</v-btn
                >
              </v-container>
              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="dialog = false">
                  Отмена
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card>
        <v-btn :disabled="!signatureSaved" color="primary" @click="finishStep2">
          Подтвердить корректность подписи и получение посылки
        </v-btn>
        <v-btn text @click="goToStep1"> Вернуться на предыдущий шаг </v-btn>
      </v-stepper-content>

      <v-stepper-step step="3" :complete="step3Complete">
        Шаг 3. Попросите заказчика подтвердить передачу посылки и оставить
        подпись
      </v-stepper-step>

      <v-stepper-content step="3">
        <v-card color="" class="mb-12">
          <v-btn
            class="mb-5"
            color="dark"
            dark
            @click="openModalStep3()"
            v-if="!signatureSaved"
          >
            Нажмите и передайте устройство заказчику
          </v-btn>
          <div v-else>
            <h4>Подпись заказчика</h4>
            <img height="300" :src="base64img" alt="" /><br />
            <v-btn class="mb-5" text @click="retry()">
              Повторить процедуру
            </v-btn>
          </div>

          <v-dialog v-model="dialogStep3" width="500">
            <v-card>
              <v-card-title class="text-h5 grey lighten-2">
                Пожалуйста, оставьте подпись
              </v-card-title>

              <v-card-text class="mt-2 pb-0">
                Оставляя подпись, вы подтверждаете передачу посылки курьеру
              </v-card-text>
              <v-container fluid>
                <h2>Распишитесь в окошке ниже и сохраните подпись в системе</h2>
                <canvas id="canvasStep3"></canvas><br />
                <v-btn text @click="signatureSavePng">
                  Сохранить как png
                </v-btn>
                <v-btn text @click="signatureClear"> Очистить </v-btn><br />
                <v-btn @click="signatureSaveInDbStep3"
                  >Сохранить подпись в системе</v-btn
                >
              </v-container>
              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="dialog = false">
                  Отмена
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card>
        <v-btn :disabled="!signatureSaved" color="primary" @click="finishStep3">
          Подтвердить корректность подписи и получение посылки курьером
        </v-btn>
        <v-btn text @click="goToStep2"> Вернуться на предыдущий шаг </v-btn>
      </v-stepper-content>

      <v-stepper-step step="4" :complete="step4Complete">
        Шаг 4. Доставьте посылку получателю
      </v-stepper-step>

      <v-stepper-content step="4">
        <v-card class="mb-12" height="300px">
          <MapTwoDots :to="order.pointTo"></MapTwoDots>
        </v-card>
        <v-btn color="primary" @click="finishStep4">
          Подтвердить нахождение в месте назначения
        </v-btn>
        <v-btn text @click="goToStep3"> Вернуться на предыдущий шаг </v-btn>
      </v-stepper-content>

      <v-stepper-step step="5" :complete="step5Complete">
        Шаг 5. Попросите документ, удостоверяющий личность и проверьте данные
      </v-stepper-step>

      <v-stepper-content step="5">
        <v-container>
          <v-row>
            <v-col cols="6" md="6" sm="12"
              ><div class="pt-4 pb-4">
                <h4 class="mb-4 text-left">
                  Подробно о заказе №{{ order.id }}
                </h4>
                <p class="text-left">
                  <strong>От:</strong><br />{{ order.address_from }}
                </p>
                <p class="text-left">
                  <strong>До:</strong><br />{{ order.address_to }}
                </p>
                <p class="text-left">
                  <strong>Дата отправки:</strong><br />{{
                    order.departure_date
                  }}
                </p>
                <p class="text-left">
                  <strong>Дата получения:</strong><br />{{ order.arrival_date }}
                </p>
                <p class="text-left">
                  <strong>Кто отправлял документы:</strong><br />{{
                    order.sender
                  }}
                </p>
                <p class="text-left">
                  <strong>Кто получал документы:</strong><br />{{
                    order.recipient
                  }}
                </p>
              </div></v-col
            >
            <v-col cols="6" md="6" sm="12" align-self="center">
              <MapTwoDots
                class="mt-4 mb-4"
                :from="order.pointFrom"
                :to="order.pointTo"
              ></MapTwoDots>
            </v-col>
          </v-row>
        </v-container>
        <v-btn color="primary" @click="finishStep5">
          Подтвердить корректность данных
        </v-btn>
        <v-btn text @click="goToStep4"> Вернуться на предыдущий шаг </v-btn>
      </v-stepper-content>

      <v-stepper-step step="6" :complete="step6Complete">
        Шаг 6. Попросите получателя оставить подпись
      </v-stepper-step>

      <v-stepper-content step="6">
        <v-card color="" class="mb-12">
          <v-btn
            class="mb-5"
            color="dark"
            dark
            @click="openModal()"
            v-if="!signatureSaved"
          >
            Нажмите и передайте устройство клиенту
          </v-btn>
          <div v-else>
            <h4>Подпись клиента</h4>
            <img height="300" :src="base64img" alt="" /><br />
            <v-btn class="mb-5" text @click="retry()">
              Повторить процедуру
            </v-btn>
          </div>

          <v-dialog v-model="dialog" width="500">
            <v-card>
              <v-card-title class="text-h5 grey lighten-2">
                Пожалуйста, оставьте подпись
              </v-card-title>

              <v-card-text class="mt-2 pb-0">
                Оставляя подпись, вы подтверждаете получение товара и надлежащее
                качество обслуживания
              </v-card-text>
              <v-container fluid>
                <h2>
                  Распишитесь в окошке ниже и передайте устройство курьеру
                  обратно
                </h2>
                <canvas id="canvas"></canvas><br />
                <v-btn text @click="signatureSavePng">
                  Сохранить как png
                </v-btn>
                <v-btn text @click="signatureClear"> Очистить </v-btn><br />
                <v-btn @click="signatureSaveInDb"
                  >Сохранить подпись в системе</v-btn
                >
              </v-container>
              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="dialog = false">
                  Отмена
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card>
        <v-btn :disabled="!signatureSaved" color="primary" @click="finishStep6">
          Подтвердить корректность подписи и передачу посылки
        </v-btn>
        <v-btn text @click="goToStep5"> Вернуться на предыдущий шаг </v-btn>
      </v-stepper-content>
    </v-stepper>
    <v-card v-else class="pt-5 pb-5">
      <v-icon class="display-4 green--text">mdi-map-marker-check</v-icon>
      <h2 class="display-2 green--text mb-2">Заказ завершён!</h2>
      <h3 class="">Вами заработано: {{ order.salary_part }}</h3>
      <v-btn dark class="blue darken mt-2" to="/courier"
        ><v-icon left dark>mdi-plus</v-icon>ПРИНЯТЬ ЕЩЁ ОДИН ЗАКАЗ</v-btn
      >
    </v-card>
  </v-container>
</template>

<script>
import MapTwoDots from "../MapTwoDots";
import SignaturePad from "signature_pad";

function download(dataURL, filename) {
  if (
    navigator.userAgent.indexOf("Safari") > -1 &&
    navigator.userAgent.indexOf("Chrome") === -1
  ) {
    window.open(dataURL);
  } else {
    var blob = dataURLToBlob(dataURL);
    var url = window.URL.createObjectURL(blob);

    var a = document.createElement("a");
    a.style = "display: none";
    a.href = url;
    a.download = filename;

    document.body.appendChild(a);
    a.click();

    window.URL.revokeObjectURL(url);
  }
}

function dataURLToBlob(dataURL) {
  var parts = dataURL.split(";base64,");
  var contentType = parts[0].split(":")[1];
  var raw = window.atob(parts[1]);
  var rawLength = raw.length;
  var uInt8Array = new Uint8Array(rawLength);

  for (var i = 0; i < rawLength; ++i) {
    uInt8Array[i] = raw.charCodeAt(i);
  }

  return new Blob([uInt8Array], { type: contentType });
}
let signaturePad;
export default {
  name: "CourierSpecificOrder",
  components: { MapTwoDots },
  data() {
    return {
      dialog: false,
      success: false,
      signatureSaved: false,
      base64img: null,
      e13: 1,
      dialogStep2: false,
      dialogStep3: false,
      step1Complete: false,
      step2Complete: false,
      step3Complete: false,
      step4Complete: false,
      step5Complete: false,
      step6Complete: false,
      checkbox: false,
      order: {
        id: 1,
        departure_date: "25.03.2020",
        arrival_date: "25.03.2020",
        salary_part: "1,450 ₽",
        courier: "Иванов С.А.",
        status: "Передан курьеру",
        address_from: "г Астрахань, ул Победы, д 54",
        address_to: "г Волгоград, ул Строителей, д 12",
        sender: "Иванов Фёдор Павлович",
        recipient: "Фёдоров Павел Иванович",
        pointFrom: {
          lat: 46.355551,
          lng: 48.057676
        },
        pointTo: {
          lat: 48.606571,
          lng: 44.3626
        }
      }
    };
  },
  methods: {
    retry() {
      signaturePad.clear();
      this.base64img = null;
      this.dialog = true;
      this.signatureSaved = false;
    },
    openModal() {
      this.dialog = true;
      setTimeout(() => {
        let canvas = document.querySelector("#canvas");
        canvas.style.border = "1px dashed black";
        canvas.style.height = "300px";
        canvas.style.width = "300px";
        signaturePad = new SignaturePad(canvas);
        signaturePad.penColor = "rgb(66, 133, 244)";
        function resizeCanvas() {
          var ratio = Math.max(window.devicePixelRatio || 1, 1);
          canvas.width = canvas.offsetWidth * ratio;
          canvas.height = canvas.offsetHeight * ratio;
          canvas.getContext("2d").scale(ratio, ratio);
          signaturePad.clear();
        }

        window.onresize = resizeCanvas;
        resizeCanvas();
        resizeCanvas();
      }, 100);
    },
    openModalStep2() {
      this.dialogStep2 = true;
      setTimeout(() => {
        let canvas = document.querySelector("#canvasStep2");
        canvas.style.border = "1px dashed black";
        canvas.style.height = "300px";
        canvas.style.width = "300px";
        signaturePad = new SignaturePad(canvas);
        signaturePad.penColor = "rgb(66, 133, 244)";
        function resizeCanvas() {
          var ratio = Math.max(window.devicePixelRatio || 1, 1);
          canvas.width = canvas.offsetWidth * ratio;
          canvas.height = canvas.offsetHeight * ratio;
          canvas.getContext("2d").scale(ratio, ratio);
          signaturePad.clear();
        }

        window.onresize = resizeCanvas;
        resizeCanvas();
        resizeCanvas();
      }, 100);
    },
    openModalStep3() {
      this.dialogStep3 = true;
      setTimeout(() => {
        let canvas = document.querySelector("#canvasStep3");
        canvas.style.border = "1px dashed black";
        canvas.style.height = "300px";
        canvas.style.width = "300px";
        signaturePad = new SignaturePad(canvas);
        signaturePad.penColor = "rgb(66, 133, 244)";
        function resizeCanvas() {
          var ratio = Math.max(window.devicePixelRatio || 1, 1);
          canvas.width = canvas.offsetWidth * ratio;
          canvas.height = canvas.offsetHeight * ratio;
          canvas.getContext("2d").scale(ratio, ratio);
          signaturePad.clear();
        }

        window.onresize = resizeCanvas;
        resizeCanvas();
        resizeCanvas();
      }, 100);
    },
    async signatureSaveInDb() {
      if (signaturePad.isEmpty()) {
        alert("Пожалуйста, сначала внесите подпись");
      } else {
        console.log(signaturePad.toDataURL());
        this.base64img = signaturePad.toDataURL();
        let signature = this.base64img.split(";base64,")[1];
        console.log("!!!", signature);
        // TODO: send it to server
        try {
          let obj = {
            signature
          };
          await this.$http.post("/api/signature/", obj);
        } catch (error) {
          console.log(error);
        }
        this.dialog = false;
        this.signatureSaved = true;
      }
    },
    async signatureSaveInDbStep2() {
      if (signaturePad.isEmpty()) {
        alert("Пожалуйста, сначала внесите подпись");
      } else {
        console.log(signaturePad.toDataURL());
        this.base64img = signaturePad.toDataURL();
        let signature = this.base64img.split(";base64,")[1];
        console.log("!!!", signature);
        // TODO: send it to server
        try {
          let obj = {
            signature
          };
          await this.$http.post("/api/signature/", obj);
        } catch (error) {
          console.log(error);
        }
        this.dialogStep2 = false;
        this.signatureSaved = true;
      }
    },
    async signatureSaveInDbStep3() {
      if (signaturePad.isEmpty()) {
        alert("Пожалуйста, сначала внесите подпись");
      } else {
        console.log(signaturePad.toDataURL());
        this.base64img = signaturePad.toDataURL();
        let signature = this.base64img.split(";base64,")[1];
        console.log("!!!", signature);
        // TODO: send it to server
        try {
          let obj = {
            signature
          };
          await this.$http.post("/api/signature/", obj);
        } catch (error) {
          console.log(error);
        }
        this.dialogStep3 = false;
        this.signatureSaved = true;
      }
    },
    signatureClear() {
      signaturePad.clear();
    },
    signatureSavePng() {
      if (signaturePad.isEmpty()) {
        alert("Пожалуйста, сначала внесите подпись");
      } else {
        var dataURL = signaturePad.toDataURL();
        download(dataURL, "signature.png");
      }
    },
    finishStep1() {
      this.step1Complete = true;
      this.e13 = 2;
    },
    finishStep2() {
      this.step2Complete = true;
      this.e13 = 3;
      this.base64img = null;
      signaturePad.clear();
      this.signatureSaved = false;
    },
    finishStep3() {
      this.step3Complete = true;
      this.e13 = 4;
      this.base64img = null;
      signaturePad.clear();
      this.signatureSaved = false;
    },
    finishStep4() {
      this.step4Complete = true;
      this.e13 = 5;
    },
    finishStep5() {
      this.step5Complete = true;
      this.e13 = 6;
    },
    finishStep6() {
      this.step6Complete = true;
      this.success = true;
    },
    goToStep1() {
      this.step1Complete = false;
      this.step2Complete = false;
      this.step3Complete = false;
      this.step4Complete = false;
      this.step5Complete = false;
      this.e13 = 1;
    },
    goToStep2() {
      this.step1Complete = true;
      this.step2Complete = false;
      this.step3Complete = false;
      this.step4Complete = false;
      this.step5Complete = false;
      this.e13 = 2;
    },
    goToStep3() {
      this.step1Complete = true;
      this.step2Complete = true;
      this.step3Complete = false;
      this.step4Complete = false;
      this.step5Complete = false;
      this.e13 = 3;
    },
    goToStep4() {
      this.step1Complete = true;
      this.step2Complete = true;
      this.step3Complete = true;
      this.step4Complete = false;
      this.step5Complete = false;
      this.e13 = 4;
    },
    goToStep5() {
      this.step1Complete = true;
      this.step2Complete = true;
      this.step3Complete = true;
      this.step4Complete = true;
      this.step5Complete = false;
      this.e13 = 5;
    }
  },
  mounted() {
    // let canvas = document.querySelector("canvas");
    // canvas.style.border = "1px dashed black";
    // canvas.style.height = "300px";
    // canvas.style.width = "300px";
    // signaturePad = new SignaturePad(canvas);
    // signaturePad.penColor = "rgb(66, 133, 244)";
    // function resizeCanvas() {
    //   var ratio = Math.max(window.devicePixelRatio || 1, 1);
    //   canvas.width = canvas.offsetWidth * ratio;
    //   canvas.height = canvas.offsetHeight * ratio;
    //   canvas.getContext("2d").scale(ratio, ratio);
    //   signaturePad.clear();
    // }
    // window.onresize = resizeCanvas;
    // resizeCanvas();
    // resizeCanvas();
  }
};
</script>

<style lang="scss" scoped></style>
