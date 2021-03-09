from numpy import abs as np_abs, argmin


def get_il_xl_z(zarr_handle):
    il_arr = zarr_handle['metadata/ilines'][:]
    xl_arr = zarr_handle['metadata/xlines'][:]
    samples = zarr_handle['metadata/samples'][:]

    return il_arr, xl_arr, samples


def get_inline(zarr_handle, inline):
    il_arr, xl_arr, samples = get_il_xl_z(zarr_handle)

    # Find the inline index user requested
    il_idx = argmin(np_abs(il_arr - inline))
    il_data = zarr_handle['seismic'][il_idx, ...]

    return xl_arr, samples, il_data


def get_xline(zarr_handle, xline):
    il_arr, xl_arr, samples = get_il_xl_z(zarr_handle)

    # Find the inline index user requested
    xl_idx = argmin(np_abs(xl_arr - xline))
    xl_data = zarr_handle['seismic'][:, xl_idx, :]

    return il_arr, samples, xl_data


def get_z_slice(zarr_handle, z_val):
    il_arr, xl_arr, samples = get_il_xl_z(zarr_handle)

    # Find the inline index user requested
    z_idx = argmin(np_abs(samples - z_val))
    z_data = zarr_handle['seismic'][..., z_idx]

    return il_arr, xl_arr, z_data
