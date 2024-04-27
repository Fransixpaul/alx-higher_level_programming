#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyListObject *list;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n");
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    fprintf(stdout, "[*] Python list info\n");
    fprintf(stdout, "[*] Size of the Python List = %zd\n", size);
    fprintf(stdout, "[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; ++i) {
        PyObject *element = PyList_GetItem(p, i);
        fprintf(stdout, "Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *str;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n");
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    fprintf(stdout, "[.] bytes object info\n");
    fprintf(stdout, "  size: %zd\n", size);
    fprintf(stdout, "  trying string: %s\n", str);

    fprintf(stdout, "  first %zd bytes:", (size < 10) ? size : 10);
    for (i = 0; i < ((size < 10) ? size : 10); ++i) {
        fprintf(stdout, " %02x", str[i]);
    }
    fprintf(stdout, "\n");
}

