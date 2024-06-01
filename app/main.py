from fastapi import FastAPI
from .service.bean_inference_service import BeanInferenceService
from .dto.bean_dto import BeanDto

app = FastAPI()
bean_svc = BeanInferenceService()

@app.post("/bean/predict/class")
def predict_bean_class(bean: BeanDto):
    return bean_svc.predict(bean)