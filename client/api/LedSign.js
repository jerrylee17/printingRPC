const express = require('express');
const router = express.Router();
const {
  healthCheck,
  addMessageToQueue,
  clearMessageQueue,
  deleteMessageFromQueue
} = require('../ledsign/led_sign_client');
const { OK, BAD_REQUEST, NOT_FOUND, LED_SIGN_IP } = require('../config/config');
const { addSignLog } = require('../util/logging-helpers');

router.post('/LedSign/healthCheck', (req, res) => {
  const { officerName } = req.body;
  healthCheck(officerName, LED_SIGN_IP)
    .then(response => {
      const { messages } = response;
      const messageList =
        messages.getMessagesList && messages.getMessagesList();
      return res.status(OK).send(
        messageList.map(msg => ({
          text: msg.getText(),
          brightness: msg.getBrightness(),
          scrollSpeed: msg.getScrollSpeed(),
          backgroundColor: msg.getBackgroundColor(),
          textColor: msg.getTextColor(),
          borderColor: msg.getBorderColor()
        }))
      );
    })
    .catch(error => {
      console.log(error);
      return res.status(NOT_FOUND).send({ ...error });
    });
});

router.post('/LedSign/deleteMessageFromQueue', (req, res) => {
  const { deleteMessage } = req.body;
  deleteMessageFromQueue(deleteMessage, LED_SIGN_IP)
    .then(response => {
      return res.status(OK).send({ ...response });
    })
    .catch(error => {
      console.log(error);
      return res.status(NOT_FOUND).send({ ...error });
    });
});

router.post('/LedSign/addMessageToQueue', async (req, res) => {
  if (!(await addSignLog(req.body))) {
    return res.sendStatus(BAD_REQUEST);
  }
  addMessageToQueue(req.body, LED_SIGN_IP)
    .then(response => {
      return res.status(OK).send({ ...response });
    })
    .catch(error => {
      console.log(error);
      return res.status(NOT_FOUND).send({ ...error });
    });
});

router.post('/LedSign/clearMessageQueue', (req, res) => {
  clearMessageQueue(LED_SIGN_IP)
    .then(response => {
      return res.status(OK).send({ ...response });
    })
    .catch(error => {
      return res.status(NOT_FOUND).send({ ...error });
    });
});

module.exports = router;
