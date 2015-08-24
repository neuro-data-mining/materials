import numpy as np
import pandas as pd

# Load labels
labelf = 'fs_gm.csv'
labeldf = pd.read_csv(labelf, names=['RegionName','Label'])
roinames = labeldf.RegionName.values

# Generate fake pet data
subjects = ['S%i' % (s) for s in range(1, 15)]
# PIB-PET
sub_df = pd.DataFrame(np.random.permutation(subjects)[:10], columns=['Subject'])
pib_pet_dat = np.random.gamma(shape=2., scale=0.5, size=800).reshape(10,80)
pib_pet_df = pd.concat([sub_df, pd.DataFrame(pib_pet_dat, columns=roinames)], axis=1)
pib_pet_df.to_excel('fake_pib_pet_data.xlsx')
# APOE Status
sub_df = pd.DataFrame(np.random.permutation(subjects), columns=['Subject'])
apoe_list = ['E2','E3','E4']
apoe_dat = np.random.choice(apoe_list, 30).reshape(15,2)
apoe_df = pd.concat([sub_df, pd.DataFrame(apoe_dat, \
                                              columns=['APOE_Copy1', 'APOE_Copy2'])], axis=1)
apoe_df.to_csv('fake_apoe_data.csv')
