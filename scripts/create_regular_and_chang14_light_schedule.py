'''
Takes a couple of minutes to run
'''
import numpy as np
from circadian.lights import LightSchedule

dt = 0.005 # hours
days = 14.0
lights_on = 6.0
lights_off = 22.0
chang14_indoor_lux = 90.0
chang14_dim_lux = 3.0
chang14_ereader_lux = 31.73
chang14_book_lux = 0.91
regular_indoor_lux = 1000.0
save_path = "../data/light_schedules/"

time = np.arange(0, 24*days, dt)

regular_schedule = LightSchedule.Regular(regular_indoor_lux,
                                         lights_on=lights_on,
                                         lights_off=lights_off)

chang14_ebook_first_schedule = LightSchedule.Chang14(typical_indoor_lux=chang14_indoor_lux,
                                                     dim_lux=chang14_dim_lux,
                                                     ereader_lux=chang14_ereader_lux,
                                                     book_lux=chang14_book_lux,
                                                     first_reading_condition="eReader")
chang14_ebook_second_schedule = LightSchedule.Chang14(typical_indoor_lux=chang14_indoor_lux,
                                                      dim_lux=chang14_dim_lux,
                                                      ereader_lux=chang14_ereader_lux,
                                                      book_lux=chang14_book_lux,
                                                      first_reading_condition="Book")
regular_light = regular_schedule(time)
chang14_ebook_first_light = chang14_ebook_first_schedule(time)
chang14_ebook_second_light = chang14_ebook_second_schedule(time)

np.save(f"{save_path}/time.npy", time)
np.save(f"{save_path}/regular_light.npy", regular_light)
np.save(f"{save_path}/chang14_ebook_first_light.npy", chang14_ebook_first_light)
np.save(f"{save_path}/chang14_ebook_second_light.npy", chang14_ebook_second_light)
np.savez(f"{save_path}/light_schedules_parameters.npz",
        dt=dt, days=days, lights_on=lights_on, lights_off=lights_off,
        chang14_indoor_lux=chang14_indoor_lux, chang14_dim_lux=chang14_dim_lux,
        chang14_ereader_lux=chang14_ereader_lux, chang14_book_lux=chang14_book_lux,
        regular_indoor_lux=regular_indoor_lux)