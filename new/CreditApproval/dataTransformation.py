import pandas
import numpy
from sklearn.decomposition import PCA


def dataTransformer(path=None, delimiter=','):
    data = pandas.read_csv(path, sep=delimiter, header=None)
    data.replace(to_replace='?', value=numpy.nan, inplace=True)
    # data = data.replace(to_replace=[-1], value=[numpy.nan], inplace=True)
    lst = []
    # changing the columns to type category
    for cols in data.columns:
        # data[cols].replace(to_replace=['?'], value=[" "], inplace=True)
        if data[cols].dtype.name == 'object':
            lst.append(data[cols].astype('category'))
        else:
            lst.append(data[cols].astype(float))
    # shifting the position of class column to end

    #lstt = lst[:13]
    #lstt.append(lst[31])
    '''
    # logic to reverse one hot coded columns--------------------------------------
    lstt = pandas.concat(lst[27:], axis=1)
    lstt.rename(columns={27: 0, 28: 1, 29: 2, 30: 3, 31: 4, 32: 5, 33: 6}, inplace=True)
    for cols in lstt.columns:
        lstt[cols].replace(to_replace=[1], value=[cols], inplace=True)

    lstt = lstt.sum(axis=1)
    lst1.append(pandas.DataFrame(lstt.get_values(), columns=['Class'], dtype=float))
    # ---------------------------------------------------------------------------------
    '''
    data2 = pandas.concat(lst, axis=1)
    listND = []
    # converting the categorical to numerical values
    for cols in data2.columns:
        if data2[cols].dtype.name == 'category':
            df = pandas.DataFrame((data2[cols].cat.codes + 1).tolist(), columns=[cols], dtype=float)
            # x=numpy.divide(df.get_values()-df.get_values().min(),df.get_values().max()-df.get_values().min())
            df.replace(to_replace=[-1], value=[numpy.nan], inplace=True)
            listND.append(df)
        else:
            data2[cols].replace(to_replace=[-1], value=[numpy.nan], inplace=True)
            listND.append(data2[cols])
    data3 = pandas.concat(listND, axis=1)
    # dropping the rows having missing values
    data4 = data3.dropna(how='any')

    '''
    #whitening the data
    data4x=data4[data4.columns[0:-1]]
    data4class=data4[data4.columns[-1]]
    pca=PCA(whiten=True)
    pca.fit(data4x.get_values())
    pcax=pca.transform(data4x.get_values())
    data4x=pandas.DataFrame(data=pcax,columns=data4x.columns,dtype=float)
    data4=pandas.concat([data4x,data4class],axis=1)
    data4 = data4.dropna(how='any')
    '''
    # transforming data to rans format
    maxList = []
    dataList = []
    for cols in data4.columns:
        if data4[cols].max() == data4[cols].min():
            x = data4[cols].get_values()
        else:
            x = numpy.divide(data4[cols].get_values() - data4[cols].get_values().min(),
                             data4[cols].get_values().max() - data4[cols].get_values().min())
        y = [x.max()]
        z = numpy.asarray(y + x.tolist())
        dataList.append(z)
    data5 = numpy.asarray(dataList).transpose()
    dta = pandas.DataFrame(data=data5, dtype=float)
    data6 = dta.dropna(how='any')
    numpy.savetxt(
        fname='/home/rahul/Dropbox/MyWork/RAN_CRBMv1.0/data/newDataToExplore/new/CreditApproval/RansForm.csv', X=data5, fmt='%f',
        delimiter=',')
    print('x')


if __name__ == '__main__':
    path = '/home/rahul/Dropbox/MyWork/RAN_CRBMv1.0/data/newDataToExplore/new/CreditApproval/originalData.csv'
    dataTransformer(path=path)