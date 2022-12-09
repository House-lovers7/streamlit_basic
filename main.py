import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit チュートリアル')


st.write('Display Image')

img = Image.open('sample.jpg')
st.image(img, caption='Test Image', use_column_width=True)


st.write('DataFrame')


df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

# st.table(df.style.highlight_max(axis=0))
st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)
st.map(df)


st.sidebar.write('サイドバー')

text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたのいまの調子は？', 0, 100, 50)

st.sidebar.write('サイドバ-のアウトプット')

'あなたの趣味は: ', text
'コンディション: ', condition

st.write('問い合わせボックス')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
    expander = st.expander('問いあわせ1')
    expander.write('問いあわせの回答')
    expander2 = st.expander('問いあわせ2')
    expander2.write('問いあわせの回答')
    expander3 = st.expander('問いあわせ3')
    expander3.write('問いあわせの回答')
    expander4 = st.expander('問いあわせ4')
    expander4.write('問いあわせの回答')


st.write('プログレスバー')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.2)

'Done!!!!!'


st.write('コメントアウト')


"""

# 章
## 節
### 項

``` python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
"""
``` python
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})
```
"""
