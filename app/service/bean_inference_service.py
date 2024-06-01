from joblib import load
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from pandas import DataFrame

from ..dto.bean_dto import BeanDto


class BeanInferenceService():

    model_path = 'app/model/model.joblib'
    encoder_path = 'app/encoder/encoder.joblib'

    def __init__(self):
        self.svc: SVC = load(self.model_path)
        self.encoder: LabelEncoder = load(self.encoder_path)

    def predict(self, bean: BeanDto) -> dict:
        bean_df = DataFrame.from_dict(bean).transpose()
        headers = bean_df.iloc[0]
        prepared_bean_df = DataFrame(bean_df.values[1:], columns=headers)
        print(prepared_bean_df)
        prediction = self.svc.predict(prepared_bean_df)
        classes = self.encoder.inverse_transform(prediction)
        return {"prediction": classes[0]}
